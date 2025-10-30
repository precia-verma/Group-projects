#!/usr/bin/env python3
import re

# Read the original file
with open('assets/js/mansionLevel2.js', 'r') as f:
    content = f.read()

# 1. Add sprite variables after the existing variables
sprite_vars = '''
  // Player sprite images
  const playerSprites = [];
  let spritesLoaded = 0;
  const totalSprites = 6;
  let currentSpriteIndex = 0;
  let animationCounter = 0;
  const animationSpeed = 8; // Lower = faster animation
  let lastDirection = 'right'; // Track last movement direction
'''

# Insert after "let transitionStartTime = 0;"
content = content.replace(
    'let transitionStartTime = 0;',
    'let transitionStartTime = 0;' + sprite_vars
)

# 2. Update player object to have larger size and direction tracking
player_old = '''  // Player character
  const player = {
    x: 50,
    y: 550,
    width: 30,
    height: 30,
    speed: 3,
    color: '#ff6b6b'
  };'''

player_new = '''  // Player character
  const player = {
    x: 50,
    y: 300,  // Changed from 550 to be more visible
    width: 60,  // Increased for sprite
    height: 80, // Increased for sprite
    speed: 3,
    color: '#ff6b6b',
    isMoving: false
  };'''

content = content.replace(player_old, player_new)

# 3. Add loadPlayerSprites function before loadBackground
load_sprites_func = '''
  function loadPlayerSprites() {
    console.log('Loading player sprites...');
    for (let i = 1; i <= totalSprites; i++) {
      const img = new Image();
      img.onload = function() {
        spritesLoaded++;
        console.log(`Loaded sprite ${i}/${totalSprites}`);
        if (spritesLoaded === totalSprites) {
          console.log('All player sprites loaded!');
        }
      };
      img.onerror = function() {
        console.error(`Failed to load sprite_${i}.png`);
        spritesLoaded++; // Count it anyway to not block
      };
      img.src = `assets/images/sprite_${i}.png`;
      playerSprites.push(img);
    }
  }

'''

content = content.replace(
    '  function loadBackground',
    load_sprites_func + '  function loadBackground'
)

# 4. Add loadPlayerSprites() call in initialization
content = content.replace(
    "console.log('Initializing mansion game...', { canvas });",
    "console.log('Initializing mansion game...', { canvas });\n\n    // Load player sprites\n    loadPlayerSprites();"
)

# 5. Update updatePlayer function with directional animation
update_player_old = '''  function updatePlayer() {
    // Don't update player if prompt is showing
    if (showPrompt) return;
    
    // Move player based on key presses
    if (keys.w) player.y -= player.speed;
    if (keys.s) player.y += player.speed;
    if (keys.a) player.x -= player.speed;
    if (keys.d) player.x += player.speed;

    // Keep player within canvas bounds
    player.x = Math.max(0, Math.min(canvas.width - player.width, player.x));
    player.y = Math.max(0, Math.min(canvas.height - player.height, player.y));

    // Check if player entered cemetery
    checkCemeteryCollision();
  }'''

update_player_new = '''  function updatePlayer() {
    // Don't update player if prompt is showing
    if (showPrompt) return;
    
    // Check if player is moving and determine direction
    player.isMoving = keys.w || keys.s || keys.a || keys.d;
    
    // Track direction for sprite selection
    if (keys.w || keys.a) {
      lastDirection = 'left'; // W and A use left/up sprites (1-3)
    } else if (keys.s || keys.d) {
      lastDirection = 'right'; // S and D use right/down sprites (4-6)
    }
    
    // Move player based on key presses
    if (keys.w) player.y -= player.speed;
    if (keys.s) player.y += player.speed;
    if (keys.a) player.x -= player.speed;
    if (keys.d) player.x += player.speed;

    // Update animation frame if moving
    if (player.isMoving) {
      animationCounter++;
      if (animationCounter >= animationSpeed) {
        animationCounter = 0;
        
        // Cycle through appropriate sprite range based on direction
        if (lastDirection === 'left') {
          // Sprites 0-2 (indices for sprites 1-3)
          currentSpriteIndex = (currentSpriteIndex % 3);
          currentSpriteIndex = (currentSpriteIndex + 1) % 3;
        } else {
          // Sprites 3-5 (indices for sprites 4-6)
          if (currentSpriteIndex < 3) currentSpriteIndex = 3;
          currentSpriteIndex = 3 + ((currentSpriteIndex - 3 + 1) % 3);
        }
      }
    } else {
      // When idle, show first frame of last direction
      currentSpriteIndex = lastDirection === 'left' ? 0 : 3;
      animationCounter = 0;
    }

    // Keep player within canvas bounds
    player.x = Math.max(0, Math.min(canvas.width - player.width, player.x));
    player.y = Math.max(0, Math.min(canvas.height - player.height, player.y));

    // Check if player entered cemetery
    checkCemeteryCollision();
  }'''

content = content.replace(update_player_old, update_player_new)

# 6. Update drawPlayer function to use sprites
draw_player_old_pattern = r'  function drawPlayer\(\) \{[^}]+\}[^}]+\}'
draw_player_new = '''  function drawPlayer() {
    // Draw player sprite if loaded, otherwise draw circle as fallback
    if (spritesLoaded === totalSprites && playerSprites[currentSpriteIndex]) {
      const sprite = playerSprites[currentSpriteIndex];
      
      // Draw the sprite
      ctx.drawImage(
        sprite,
        player.x,
        player.y,
        player.width,
        player.height
      );
      
      // Debug: show which sprite is being used
      if (false) { // Set to true for debugging
        ctx.fillStyle = 'yellow';
        ctx.font = '12px Arial';
        ctx.fillText(`Sprite: ${currentSpriteIndex + 1}`, player.x, player.y - 5);
      }
    } else {
      // Fallback: Draw player as a circle with outline
      ctx.fillStyle = player.color;
      ctx.strokeStyle = '#fff';
      ctx.lineWidth = 2;
      
      ctx.beginPath();
      ctx.arc(
        player.x + player.width / 2,
        player.y + player.height / 2,
        player.width / 2,
        0,
        Math.PI * 2
      );
      ctx.fill();
      ctx.stroke();

      // Draw a direction indicator (small dot)
      ctx.fillStyle = '#fff';
      ctx.beginPath();
      ctx.arc(
        player.x + player.width / 2,
        player.y + player.height / 2 - 5,
        3,
        0,
        Math.PI * 2
      );
      ctx.fill();
    }
  }'''

content = re.sub(draw_player_old_pattern, draw_player_new, content, flags=re.DOTALL)

# Write the updated content
with open('assets/js/mansionLevel2.js', 'w') as f:
    f.write(content)

print("✓ JavaScript file updated with sprite animation!")
print("✓ Sprites 1-3: Left/Up movement")
print("✓ Sprites 4-6: Right/Down movement")
print("✓ Player starting position changed to y=300 for better visibility")

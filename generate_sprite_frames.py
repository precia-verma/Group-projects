#!/usr/bin/env python3
"""
Generate 6 animated sprite frames from a single sprite image.
This creates slight variations to simulate animation.
"""

from PIL import Image, ImageDraw
import os
import sys

def create_sprite_frames(input_path, output_dir='assets/images'):
    """
    Create 6 animation frames from a sprite image.
    
    Args:
        input_path: Path to the input sprite image
        output_dir: Directory to save the frames
    """
    try:
        # Load the sprite image
        sprite = Image.open(input_path)
        print(f"✓ Loaded sprite: {input_path}")
        print(f"  Size: {sprite.size}")
        
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Frame size (you can adjust this)
        frame_width = 80
        frame_height = 80
        
        # Generate 6 frames
        for i in range(6):
            # Create a new transparent frame
            frame = Image.new('RGBA', (frame_width, frame_height), (0, 0, 0, 0))
            
            # Calculate animation variations
            # Frame 1: Normal
            # Frame 2: Slightly up
            # Frame 3: Slightly right
            # Frame 4: Normal
            # Frame 5: Slightly down  
            # Frame 6: Slightly left
            
            offsets = [
                (0, 0),      # Frame 1: center
                (0, -2),     # Frame 2: up
                (2, -1),     # Frame 3: right-up
                (0, 0),      # Frame 4: center
                (0, 2),      # Frame 5: down
                (-2, 1)      # Frame 6: left-down
            ]
            
            offset_x, offset_y = offsets[i]
            
            # Resize sprite if needed to fit in frame
            sprite_resized = sprite.copy()
            if sprite_resized.width > frame_width - 10 or sprite_resized.height > frame_height - 10:
                max_size = min(frame_width - 10, frame_height - 10)
                sprite_resized.thumbnail((max_size, max_size), Image.Resampling.LANCZOS)
            
            # Calculate position to center the sprite
            x = (frame_width - sprite_resized.width) // 2 + offset_x
            y = (frame_height - sprite_resized.height) // 2 + offset_y
            
            # Paste sprite onto frame
            if sprite_resized.mode == 'RGBA':
                frame.paste(sprite_resized, (x, y), sprite_resized)
            else:
                frame.paste(sprite_resized, (x, y))
            
            # Save the frame
            output_path = os.path.join(output_dir, f'character_frame_{i+1}.png')
            frame.save(output_path)
            print(f"✓ Created frame {i+1}: {output_path}")
        
        print(f"\n🎉 Success! Created 6 sprite frames in {output_dir}")
        print("\nYou can now test the game by opening mansion2.html")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 generate_sprite_frames.py <sprite_image_path>")
        print("\nExample:")
        print("  python3 generate_sprite_frames.py player-sprite.png")
        print("  python3 generate_sprite_frames.py assets/images/player-sprite.png")
        sys.exit(1)
    
    input_sprite = sys.argv[1]
    
    if not os.path.exists(input_sprite):
        print(f"❌ Error: File not found: {input_sprite}")
        sys.exit(1)
    
    create_sprite_frames(input_sprite)

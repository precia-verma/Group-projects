---
layout: default
title:  Snake Game 2.0
permalink: /snake
---

<style>
    body{
    }
    .wrap{
        margin-left: auto;
        margin-right: auto;
    }

    /* Scope canvas styles to the snake canvas only to avoid colliding with other pages */
    #snake_canvas{
        border: 3px solid #444444;
        margin: 20px auto;
        display: block;
        width: 320px;
        height: 320px;
        max-width: 90vw;
        max-height: 70vh;
        background-color: #2F4F2F;
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.3);
        transition: width 0.5s ease-in-out, height 0.5s ease-in-out;
    }
    #snake_canvas.hidden{
        display: none !important;
    }
    #snake_canvas:focus{
        outline: none;
    }

    /* All screens style */
    #snake_gameover p, #snake_setting p, #snake_menu p{
        font-size: 20px;
    }

    /* style both anchors and buttons used as menu controls */
    #snake_gameover a, #snake_gameover button, #snake_setting a, #snake_setting button, #snake_menu a, #snake_menu button{
        font-size: 30px;
        display: block;
        background: transparent;
        border: none;
        color: inherit;
        text-align: center;
        padding: 8px 0;
        font-family: inherit;
        cursor: pointer;
        pointer-events: auto;
        user-select: none;
    }

    /* Ensure buttons with link-alert class are clickable */
    button.link-alert {
        cursor: pointer !important;
        pointer-events: auto !important;
        border: 1px solid transparent;
        transition: all 0.2s ease;
    }

    button.link-alert:hover {
        background-color: rgba(255, 255, 255, 0.1);
        border-color: rgba(255, 255, 255, 0.3);
    }

    #snake_gameover a:hover, #snake_gameover button:hover, #snake_setting a:hover, #snake_setting button:hover, #snake_menu a:hover, #snake_menu button:hover{
        cursor: pointer;
    }

    #snake_gameover a:hover::before, #snake_gameover button:hover::before, #snake_setting a:hover::before, #snake_setting button:hover::before, #snake_menu a:hover::before, #snake_menu button:hover::before{
        content: ">";
        margin-right: 10px;
    }

    #snake_menu{
        display: block;
    }

    #snake_gameover{
        display: none;
    }

    #snake_setting{
        display: none;
    }

    #snake_setting input{
        display:none;
    }

    #snake_setting label{
        cursor: pointer;
    }

    #snake_setting input:checked + label{
        background-color: #FFF;
        color: #000;
    }

    /* Special styling for extreme speed modes */
    #speed0:checked + label{
        background-color: #90EE90;
        color: #000;
    }

    #speed4:checked + label{
        background-color: #FF4500;
        color: #FFF;
        animation: pulse 1s infinite;
    }

    /* Scoreboard animations */
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }

    @keyframes scoreUpdate {
        0% { transform: scale(1); }
        50% { transform: scale(1.2); color: #FFD700; }
        100% { transform: scale(1); }
    }

    .score-update {
        animation: scoreUpdate 0.3s ease-in-out;
    }
</style>

<h2>Snake</h2>
<div class="container">
    <!-- Simplified Scoreboard -->
    <div style="text-align: center; margin: 20px 0; padding: 10px; background: #333; color: white; border-radius: 10px;">
        <span>Score: <span id="snake_score_value">0</span></span> | 
    <span>Length: <span id="snake_snake_length">1</span></span> | 
    <span>Level: <span id="snake_game_level">1</span></span> | 
    <span>Lives: <span id="snake_lives_value">0</span></span> | 
    <span>Best: <span id="snake_high_score">0</span></span>
        <br>
        <span style="color: #87CEEB;">Map Size: <span id="snake_map_size">320x320</span></span> | 
        <span style="color: #90EE90;">Next Expansion: <span id="snake_next_expansion">Length 10</span></span>
        <div id="snake_achievement_banner" style="margin-top: 10px; color: gold; display: none;">
            🎉 <span id="snake_achievement_text"></span> 🎉
        </div>
    </div>
    
    <!-- Food Legend -->
    <div style="text-align: center; margin: 10px 0; padding: 8px; background: #222; color: white; border-radius: 8px; font-size: 12px;">
        <strong>Food Types:</strong> 
        <span style="color: #FF4444;">🍎 Apple (+1)</span> | 
        <span style="color: #FF69B4;">🍩 Donut (+2)</span> | 
        <span style="color: #FFD700;">🍕 Pizza (+3)</span> | 
        <span style="color: #8B4513;">🍔 Hamburger (+5)</span> | 
        <span style="color: #A0522D;">🥩 Steak (+8)</span> | 
        <span style="color: #FF1493;">🎂 Cake (+10)</span>
        <br>
        <strong>Special Blocks:</strong>
        <span style="color: #FF4500;">🔥 Lava (-1 Length)</span> | 
        <span style="color: #696969;">⬛ Wall (Death)</span> | 
        <span style="color: #FF0000;">🐍 Enemy Snake (Death)</span>
    </div>
    <div class="container bg-secondary" style="text-align:center;">
        <!-- Main Menu -->
    <div id="snake_menu" class="py-4 text-light">
            <p>Welcome to Snake, press <span style="background-color: #FFFFFF; color: #000000">space</span> to begin</p>
            <button id="snake_new_game" class="link-alert" type="button">new game</button>
            <button id="snake_setting_menu" class="link-alert" type="button">settings</button>
        </div>
        <!-- Game Over -->
        <div id="snake_gameover" class="py-4 text-light">
            <p>Game Over, press <span style="background-color: #FFFFFF; color: #000000">space</span> to try again</p>
            <button id="snake_new_game1" class="link-alert" type="button">new game</button>
            <button id="snake_setting_menu1" class="link-alert" type="button">settings</button>
        </div>
        <!-- Play Screen -->
    <canvas id="snake_canvas" class="wrap hidden" width="320" height="320" tabindex="1"></canvas>
        <!-- Settings Screen -->
        <div id="snake_setting" class="py-4 text-light">
            <p>Settings Screen, press <span style="background-color: #FFFFFF; color: #000000">space</span> to go back to playing</p>
            <button id="snake_new_game2" class="link-alert" type="button">new game</button>
            <br>
            <p>Speed:
                <input id="snake_speed0" type="radio" name="snake_speed" value="300"/>
                <label for="snake_speed0">Grandma</label>
                <input id="snake_speed1" type="radio" name="snake_speed" value="120"/>
                <label for="snake_speed1">Slow</label>
                <input id="snake_speed2" type="radio" name="snake_speed" value="75" checked/>
                <label for="snake_speed2">Normal</label>
                <input id="snake_speed3" type="radio" name="snake_speed" value="35"/>
                <label for="snake_speed3">Fast</label>
                <input id="snake_speed4" type="radio" name="snake_speed" value="10"/>
                <label for="snake_speed4">Impossible</label>
            </p>
            <p>Wall:
                <input id="snake_wallon" type="radio" name="snake_wall" value="1" checked/>
                <label for="snake_wallon">On</label>
                <input id="snake_walloff" type="radio" name="snake_wall" value="0"/>
                <label for="snake_walloff">Off</label>
            </p>
            <p>Internal Walls:
                <input id="snake_internalwalls_off" type="radio" name="snake_internal_walls" value="0" checked/>
                <label for="snake_internalwalls_off">Off</label>
                <input id="snake_internalwalls_few" type="radio" name="snake_internal_walls" value="1"/>
                <label for="snake_internalwalls_few">Few</label>
                <input id="snake_internalwalls_many" type="radio" name="snake_internal_walls" value="2"/>
                <label for="snake_internalwalls_many">Many</label>
            </p>
            <p>Challenge Mode:
                <input id="snake_challengeon" type="checkbox" name="snake_challenge" />
                <label for="snake_challengeon">Enable Challenge Mode (reverse controls: ↑→↓, ↓→↑, ←→→, →→←)</label>
            </p>
            <p>Lava Challenge:
                <input id="snake_lava_challenge" type="checkbox" name="snake_lava_challenge" />
                <label for="snake_lava_challenge">Enable Lava Challenge (lava blocks reduce snake length by 1)</label>
            </p>
            <p>Enemies Mode:
                <input id="snake_enemies_mode" type="checkbox" name="snake_enemies_mode" />
                <label for="snake_enemies_mode">Enable Enemies (red snakes chase you and cause death on contact)</label>
            </p>
        </div>

<div id="snake_debug" style="position:fixed;right:12px;bottom:12px;background:rgba(0,0,0,0.7);color:#fff;padding:8px;border-radius:6px;font-family:monospace;z-index:9999;display:none;min-width:160px;">snake debug</div>
<script>
// Complete Snake Game Implementation
(function(){
    'use strict';

    const BLOCK = 10;
    const SCREEN_SNAKE = 0, SCREEN_MENU = -1, SCREEN_GAME_OVER = 1, SCREEN_SETTING = 2;
    let SCREEN = SCREEN_MENU;

    // Food types with different effects and spawn chances
    const FOOD_TYPES = {
        apple: { growth: 1, score: 1, chance: 50, color: '#FF4444', name: 'Apple' },
        donut: { growth: 2, score: 2, chance: 25, color: '#FF69B4', name: 'Donut' },
        hamburger: { growth: 5, score: 5, chance: 15, color: '#8B4513', name: 'Hamburger' },
        pizza: { growth: 3, score: 3, chance: 20, color: '#FFD700', name: 'Pizza' },
        steak: { growth: 8, score: 10, chance: 5, color: '#A0522D', name: 'Steak' },
        cake: { growth: 10, score: 15, chance: 2, color: '#FF1493', name: 'Cake' }
    };

    let canvas = null, ctx = null;
    let screen_menu = null, screen_game_over = null, screen_setting = null;
    let ele_score = null, ele_snake_length = null, ele_game_level = null, ele_high_score = null, ele_lives = null;
    let ele_achievement_banner = null, ele_achievement_text = null;
    let ele_map_size = null, ele_next_expansion = null;
    let speed_setting = null, wall_setting = null, internal_walls_setting = null;
    let btn_new_game = null, btn_new_game1 = null, btn_new_game2 = null, btn_setting_menu = null, btn_setting_menu1 = null;

    let snake = null;
    let snake_dir = 1, snake_next_dir = 1;
    let snake_speed = 75;
    let lives = 3;
    let foods = [];
    let walls = []; // Internal walls array
    let lavaBlocks = []; // Lava challenge blocks array
    let enemies = []; // Enemy snakes array
    let score = 0;
    let game_level = 1;
    let high_score = parseInt(localStorage.getItem('snake_high_score')) || 0;
    let wall = 1;
    let internal_walls = 0; // Setting for internal walls
    let gameTimer = null;
    let challengeMode = false;
    let lavaChallengeMode = false;
    let enemiesMode = false;
    
    // Map expansion variables
    let currentMapWidth = 320;
    let currentMapHeight = 320;
    let expansionThresholds = [10, 25, 50, 75, 100]; // Snake lengths that trigger expansion
    let expansionsCompleted = 0;

    function $id(id){ return document.getElementById(id); }

    function setDebug(msg){
        console.log('Snake Debug:', msg);
        const d = $id('snake_debug');
        if(!d) return;
        d.style.display = 'block';
        const now = new Date().toLocaleTimeString();
        const prev = d.innerText || '';
        const lines = prev.split('\n').filter(Boolean);
        lines.unshift(now + ' - ' + msg);
        d.innerText = lines.slice(0,6).join('\n');
    }

    function showScreen(s){
        setDebug('showScreen called with: ' + s);
        SCREEN = s;
        const c = $id('snake_canvas');
        if(c){
            if(s===SCREEN_MENU) {
                c.classList.add('hidden');
            } else {
                c.classList.remove('hidden');
            }
        }
        if(screen_menu) screen_menu.style.display = (s===SCREEN_MENU)?'block':'none';
        if(screen_game_over) screen_game_over.style.display = (s===SCREEN_GAME_OVER)?'block':'none';
        if(screen_setting) screen_setting.style.display = (s===SCREEN_SETTING)?'block':'none';
    }

    function init(){
        setDebug('Initializing snake game');
        
        canvas = $id('snake_canvas');
        if(canvas){ 
            canvas.width = 320; 
            canvas.height = 320; 
            ctx = canvas.getContext('2d'); 
        }
        
        screen_menu = $id('snake_menu'); 
        screen_game_over = $id('snake_gameover'); 
        screen_setting = $id('snake_setting');
        
        ele_score = $id('snake_score_value'); 
        ele_snake_length = $id('snake_snake_length'); 
        ele_game_level = $id('snake_game_level'); 
        ele_high_score = $id('snake_high_score'); 
        ele_lives = $id('snake_lives_value');
        ele_achievement_banner = $id('snake_achievement_banner'); 
        ele_achievement_text = $id('snake_achievement_text');
        ele_map_size = $id('snake_map_size');
        ele_next_expansion = $id('snake_next_expansion');
        
        speed_setting = document.getElementsByName('snake_speed'); 
        wall_setting = document.getElementsByName('snake_wall');
        internal_walls_setting = document.getElementsByName('snake_internal_walls');
        
        btn_new_game = $id('snake_new_game'); 
        btn_new_game1 = $id('snake_new_game1'); 
        btn_new_game2 = $id('snake_new_game2'); 
        btn_setting_menu = $id('snake_setting_menu'); 
        btn_setting_menu1 = $id('snake_setting_menu1');

        if(ele_high_score) ele_high_score.innerText = String(high_score);
        
        // Add event listeners
        if(btn_new_game) btn_new_game.onclick = function(e){ e.preventDefault(); newGame(); };
        if(btn_new_game1) btn_new_game1.onclick = function(e){ e.preventDefault(); newGame(); };
        if(btn_new_game2) btn_new_game2.onclick = function(e){ e.preventDefault(); newGame(); };
        if(btn_setting_menu) btn_setting_menu.onclick = function(e){ e.preventDefault(); showScreen(SCREEN_SETTING); };
        if(btn_setting_menu1) btn_setting_menu1.onclick = function(e){ e.preventDefault(); showScreen(SCREEN_SETTING); };

        // Speed settings
        if(speed_setting && speed_setting.length){
            for(let i=0;i<speed_setting.length;i++){
                speed_setting[i].addEventListener('click', function(){
                    for(let k=0;k<speed_setting.length;k++) {
                        if(speed_setting[k].checked){ 
                            setSnakeSpeed(speed_setting[k].value); 
                            computeLives(); 
                            break; 
                        }
                    }
                });
            }
        }

        // Wall settings
        if(wall_setting && wall_setting.length){
            for(let i=0;i<wall_setting.length;i++){
                wall_setting[i].addEventListener('click', function(){ 
                    for(let k=0;k<wall_setting.length;k++) {
                        if(wall_setting[k].checked) setWall(wall_setting[k].value); 
                    }
                });
            }
        }

        // Internal walls settings
        if(internal_walls_setting && internal_walls_setting.length){
            for(let i=0;i<internal_walls_setting.length;i++){
                internal_walls_setting[i].addEventListener('click', function(){ 
                    for(let k=0;k<internal_walls_setting.length;k++) {
                        if(internal_walls_setting[k].checked) {
                            internal_walls = parseInt(internal_walls_setting[k].value);
                            break;
                        }
                    }
                });
            }
        }

        // Challenge mode
        const challenge = $id('snake_challengeon'); 
        if(challenge) challenge.addEventListener('change', function(){ 
            challengeMode = this.checked; 
            computeLives(); 
        });

        // Lava challenge mode
        const lavaChallenge = $id('snake_lava_challenge');
        if(lavaChallenge) lavaChallenge.addEventListener('change', function(){
            lavaChallengeMode = this.checked;
            if(lavaChallengeMode && snake) {
                generateLavaBlocks();
            } else {
                lavaBlocks = [];
            }
        });

        // Enemies mode
        const enemiesModeCheckbox = $id('snake_enemies_mode');
        if(enemiesModeCheckbox) enemiesModeCheckbox.addEventListener('change', function(){
            enemiesMode = this.checked;
            if(enemiesMode && snake) {
                spawnEnemies();
            } else {
                enemies = [];
            }
        });

        // Keyboard controls
        window.addEventListener('keydown', function(evt){
            if(evt.code === 'Space' && SCREEN !== SCREEN_SNAKE) { 
                evt.preventDefault(); 
                newGame(); 
            }
            if(SCREEN === SCREEN_SNAKE) changeDir(evt.keyCode);
        });

        showScreen(SCREEN_MENU);
        setDebug('Initialization complete');
    }

    function expandMap() {
        if(!canvas) return;
        
        // Increase map size by 80 pixels (8 blocks) in each direction
        currentMapWidth += 80;
        currentMapHeight += 80;
        
        // Update canvas size
        canvas.width = currentMapWidth;
        canvas.height = currentMapHeight;
        canvas.style.width = currentMapWidth + 'px';
        canvas.style.height = currentMapHeight + 'px';
        
        expansionsCompleted++;
        
        // Show achievement for map expansion
        showAchievement(`🗺️ MAP EXPANDED! Level ${expansionsCompleted} 🗺️`);
        
        // Regenerate walls and add more food after expansion
        generateInternalWalls();
        if(lavaChallengeMode) {
            generateLavaBlocks();
        }
        if(enemiesMode) {
            spawnEnemies();
        }
        
        // Add more food based on expansion level - more food for larger maps
        const foodToAdd = 2 + expansionsCompleted; // Start with 3 foods, then 4, 5, 6, 7...
        for(let i = 0; i < foodToAdd; i++) {
            addSingleFood();
        }
        
        setDebug(`Map expanded to ${currentMapWidth}x${currentMapHeight}`);
    }

    function checkMapExpansion() {
        if(!snake || expansionsCompleted >= expansionThresholds.length) return;
        
        const currentThreshold = expansionThresholds[expansionsCompleted];
        if(snake.length >= currentThreshold) {
            expandMap();
        }
    }

    function newGame(keep){ 
        setDebug('Starting new game'); 
        showScreen(SCREEN_SNAKE); 
        try{ 
            if(canvas) canvas.focus();
        }catch(e){}
        
        // Store current snake length if keeping progress
        let preservedLength = 1;
        if(keep === true && snake && snake.length > 1) {
            preservedLength = snake.length;
        }
        
        snake = [{x:16,y:16}];
        
        // Restore snake length if keeping progress
        if(keep === true && preservedLength > 1) {
            for(let i = 1; i < preservedLength; i++) {
                snake.push({x:16,y:16});
            }
        }
        
        snake_dir = 1; 
        snake_next_dir = 1;
        if(keep!==true) { 
            score = 0; 
            game_level = 1; 
            computeLives();
            
            // Reset map size for new game
            currentMapWidth = 320;
            currentMapHeight = 320;
            expansionsCompleted = 0;
            if(canvas) {
                canvas.width = currentMapWidth;
                canvas.height = currentMapHeight;
                canvas.style.width = currentMapWidth + 'px';
                canvas.style.height = currentMapHeight + 'px';
            }
            
            generateInternalWalls(); // Generate walls when starting new game
            if(lavaChallengeMode) {
                generateLavaBlocks(); // Generate lava blocks if challenge is enabled
            }
            if(enemiesMode) {
                spawnEnemies(); // Spawn enemy snakes if enemies mode is enabled
            }
        }
        updateStats(score); 
        addFood(); 
        drawGame(); 
        if(gameTimer) clearTimeout(gameTimer); 
        gameTimer = setTimeout(mainLoop, snake_speed);
    }

    function mainLoop(){
        if(!snake || !snake.length) return;
        let x = snake[0].x, y = snake[0].y;
        snake_dir = snake_next_dir;
        switch(snake_dir){ 
            case 0: y--; break; 
            case 1: x++; break; 
            case 2: y++; break; 
            case 3: x--; break; 
        }
        snake.pop(); 
        snake.unshift({x:x,y:y});

        const cols = Math.max(1, Math.floor(currentMapWidth / BLOCK));
        const rows = Math.max(1, Math.floor(currentMapHeight / BLOCK));

        if(wall===1){
            if(x<0 || x>=cols || y<0 || y>=rows){
                lives--; 
                updateStats(score);
                if(lives>0){ 
                    newGame(true); 
                    return; 
                } else { 
                    showScreen(SCREEN_GAME_OVER); 
                    return; 
                }
            }
        } else {
            for(let i=0;i<snake.length;i++){
                if(snake[i].x<0) snake[i].x+=cols;
                if(snake[i].x>=cols) snake[i].x-=cols;
                if(snake[i].y<0) snake[i].y+=rows;
                if(snake[i].y>=rows) snake[i].y-=rows;
            }
        }

        for(let i=1;i<snake.length;i++) {
            if(snake[0].x===snake[i].x && snake[0].y===snake[i].y){ 
                lives--; 
                updateStats(score); 
                if(lives>0){ 
                    newGame(true); 
                    return; 
                } else { 
                    showScreen(SCREEN_GAME_OVER); 
                    return; 
                } 
            }
        }

        // Check collision with internal walls
        for(let i=0; i<walls.length; i++) {
            if(snake[0].x === walls[i].x && snake[0].y === walls[i].y) {
                lives--; 
                updateStats(score); 
                if(lives>0){ 
                    newGame(true); 
                    return; 
                } else { 
                    showScreen(SCREEN_GAME_OVER); 
                    return; 
                }
            }
        }

        // Check collision with lava blocks
        for(let i=0; i<lavaBlocks.length; i++) {
            if(snake[0].x === lavaBlocks[i].x && snake[0].y === lavaBlocks[i].y) {
                // Reduce snake length by 1 when touching lava
                if(snake.length > 1) {
                    snake.pop(); // Remove last segment
                    showAchievement('🔥 LAVA BURN! -1 Length 🔥');
                } else {
                    // If snake length is 1, treat it like death
                    lives--;
                    updateStats(score);
                    if(lives > 0) {
                        newGame(true);
                        return;
                    } else {
                        showScreen(SCREEN_GAME_OVER);
                        return;
                    }
                }
                break;
            }
        }

        // Check collision with enemy snakes
        for(let e=0; e<enemies.length; e++) {
            for(let seg=0; seg<enemies[e].body.length; seg++) {
                if(snake[0].x === enemies[e].body[seg].x && snake[0].y === enemies[e].body[seg].y) {
                    lives--;
                    updateStats(score);
                    showAchievement('💀 ENEMY COLLISION! 💀');
                    if(lives > 0) {
                        newGame(true);
                        return;
                    } else {
                        showScreen(SCREEN_GAME_OVER);
                        return;
                    }
                }
            }
        }

        for(let i=0;i<foods.length;i++){
            if(checkBlock(snake[0].x, snake[0].y, foods[i].x, foods[i].y)){
                const foodType = FOOD_TYPES[foods[i].type];
                let grow = foodType.growth;
                for(let j=0;j<grow;j++) snake.push({x:snake[0].x, y:snake[0].y});
                score += foodType.score; 
                updateStats(score);
                showAchievement(`+${foodType.growth} ${foodType.name}!`);
                
                // Check for map expansion after growing
                checkMapExpansion();
                
                // Remove eaten food and add new food based on snake length
                foods.splice(i, 1);
                addSingleFood();
                break;
            }
        }

        // Update enemy snakes
        updateEnemies();

        drawGame(); 
        if(gameTimer) clearTimeout(gameTimer); 
        gameTimer = setTimeout(mainLoop, snake_speed);
    }

    function drawGame(){ 
        if(!ctx) return;
        ctx.fillStyle = '#2F4F2F'; 
        ctx.fillRect(0,0,currentMapWidth,currentMapHeight);
        
        // Draw internal walls
        for(let i=0; i<walls.length; i++) {
            drawWallBlock(walls[i].x, walls[i].y);
        }
        
        // Draw lava blocks
        for(let i=0; i<lavaBlocks.length; i++) {
            drawLavaBlock(lavaBlocks[i].x, lavaBlocks[i].y);
        }
        
        // Draw enemy snakes
        for(let e=0; e<enemies.length; e++) {
            drawEnemySnake(enemies[e]);
        }
        
        if(snake && snake.length) {
            for(let i=0;i<snake.length;i++) activeDot(snake[i].x, snake[i].y);
        }
        for(let i=0;i<foods.length;i++) activeDot(foods[i].x, foods[i].y, foods[i].type);
    }

    function changeDir(key){ 
        if(!snake) return;
        const LEFT = 37, UP = 38, RIGHT = 39, DOWN = 40;
        
        if(challengeMode) {
            // Swapped controls for challenge mode
            switch(key){
                case LEFT: if(snake_dir!==3) snake_next_dir = 1; break;  // Left -> Right
                case UP: if(snake_dir!==0) snake_next_dir = 2; break;    // Up -> Down
                case RIGHT: if(snake_dir!==1) snake_next_dir = 3; break; // Right -> Left
                case DOWN: if(snake_dir!==2) snake_next_dir = 0; break;  // Down -> Up
                case 65: if(snake_dir!==3) snake_next_dir=1; break; // A -> Right
                case 87: if(snake_dir!==0) snake_next_dir=2; break; // W -> Down
                case 68: if(snake_dir!==1) snake_next_dir=3; break; // D -> Left
                case 83: if(snake_dir!==2) snake_next_dir=0; break; // S -> Up
            }
        } else {
            // Normal controls
            switch(key){
                case LEFT: if(snake_dir!==1) snake_next_dir = 3; break;
                case UP: if(snake_dir!==2) snake_next_dir = 0; break;
                case RIGHT: if(snake_dir!==3) snake_next_dir = 1; break;
                case DOWN: if(snake_dir!==0) snake_next_dir = 2; break;
                case 65: if(snake_dir!==1) snake_next_dir=3; break; // A
                case 87: if(snake_dir!==2) snake_next_dir=0; break; // W
                case 68: if(snake_dir!==3) snake_next_dir=1; break; // D
                case 83: if(snake_dir!==0) snake_next_dir=2; break; // S
            }
        }
    }

    function activeDot(x,y,type){ 
        if(!ctx) return; 
        const px = x*BLOCK, py = y*BLOCK;
        const centerX = px + BLOCK/2;
        const centerY = py + BLOCK/2;
        
        if(type && FOOD_TYPES[type]){
            const foodType = FOOD_TYPES[type];
            
            if(type === 'apple') {
                // Draw apple shape
                ctx.fillStyle = '#FF4444';
                ctx.beginPath();
                ctx.arc(centerX, centerY + 1, BLOCK/2 - 1, 0, 2 * Math.PI);
                ctx.fill();
                
                // Apple highlight
                ctx.fillStyle = '#FF6666';
                ctx.beginPath();
                ctx.arc(centerX - 1, centerY - 1, BLOCK/4, 0, 2 * Math.PI);
                ctx.fill();
                
                // Apple stem
                ctx.fillStyle = '#654321';
                ctx.fillRect(centerX - 1, py + 1, 2, 3);
                
                // Apple leaf
                ctx.fillStyle = '#228B22';
                ctx.beginPath();
                ctx.ellipse(centerX + 2, py + 2, 2, 1, Math.PI/4, 0, 2 * Math.PI);
                ctx.fill();
                
            } else if(type === 'donut') {
                // Draw donut
                ctx.fillStyle = '#FF69B4';
                ctx.beginPath();
                ctx.arc(centerX, centerY, BLOCK/2 - 1, 0, 2 * Math.PI);
                ctx.fill();
                
                // Donut hole
                ctx.fillStyle = '#2F4F2F';
                ctx.beginPath();
                ctx.arc(centerX, centerY, BLOCK/4, 0, 2 * Math.PI);
                ctx.fill();
                
                // Donut glaze highlights
                ctx.fillStyle = '#FFB6C1';
                for(let i = 0; i < 6; i++) {
                    const angle = (i * Math.PI) / 3;
                    const glazeX = centerX + Math.cos(angle) * (BLOCK/3);
                    const glazeY = centerY + Math.sin(angle) * (BLOCK/3);
                    ctx.fillRect(glazeX, glazeY, 1, 1);
                }
                
            } else if(type === 'hamburger') {
                // Bottom bun
                ctx.fillStyle = '#D2691E';
                ctx.beginPath();
                ctx.arc(centerX, py + BLOCK - 2, BLOCK/2 - 1, 0, Math.PI);
                ctx.fill();
                
                // Meat patty
                ctx.fillStyle = '#8B4513';
                ctx.fillRect(px + 1, py + BLOCK/2, BLOCK - 2, 3);
                
                // Lettuce
                ctx.fillStyle = '#228B22';
                ctx.fillRect(px + 1, py + BLOCK/2 - 1, BLOCK - 2, 1);
                
                // Cheese
                ctx.fillStyle = '#FFD700';
                ctx.fillRect(px + 1, py + BLOCK/2 + 1, BLOCK - 2, 1);
                
                // Top bun
                ctx.fillStyle = '#DEB887';
                ctx.beginPath();
                ctx.arc(centerX, py + 3, BLOCK/2 - 1, Math.PI, 2 * Math.PI);
                ctx.fill();
                
                // Sesame seeds
                ctx.fillStyle = '#F5DEB3';
                ctx.fillRect(centerX - 2, py + 2, 1, 1);
                ctx.fillRect(centerX + 1, py + 1, 1, 1);
                ctx.fillRect(centerX, py + 3, 1, 1);
                
            } else if(type === 'pizza') {
                // Pizza base (triangle slice)
                ctx.fillStyle = '#FFD700';
                ctx.beginPath();
                ctx.moveTo(centerX, py + 1);
                ctx.lineTo(px + 1, py + BLOCK - 1);
                ctx.lineTo(px + BLOCK - 1, py + BLOCK - 1);
                ctx.closePath();
                ctx.fill();
                
                // Pizza sauce
                ctx.fillStyle = '#FF6347';
                ctx.beginPath();
                ctx.moveTo(centerX, py + 2);
                ctx.lineTo(px + 2, py + BLOCK - 2);
                ctx.lineTo(px + BLOCK - 2, py + BLOCK - 2);
                ctx.closePath();
                ctx.fill();
                
                // Pepperoni
                ctx.fillStyle = '#DC143C';
                ctx.beginPath();
                ctx.arc(centerX - 1, py + 5, 1, 0, 2 * Math.PI);
                ctx.fill();
                ctx.beginPath();
                ctx.arc(centerX + 2, py + 6, 1, 0, 2 * Math.PI);
                ctx.fill();
                
                // Cheese highlights
                ctx.fillStyle = '#FFFACD';
                ctx.fillRect(centerX - 2, py + 4, 1, 1);
                ctx.fillRect(centerX + 1, py + 7, 1, 1);
                
            } else if(type === 'steak') {
                // Steak shape (irregular oval)
                ctx.fillStyle = '#A0522D';
                ctx.beginPath();
                ctx.ellipse(centerX, centerY, BLOCK/2 - 1, BLOCK/3, 0, 0, 2 * Math.PI);
                ctx.fill();
                
                // Grill marks
                ctx.fillStyle = '#654321';
                ctx.fillRect(px + 2, py + 3, BLOCK - 4, 1);
                ctx.fillRect(px + 2, py + 6, BLOCK - 4, 1);
                
                // Fat marbling
                ctx.fillStyle = '#F5F5DC';
                ctx.fillRect(centerX - 1, py + 2, 1, 2);
                ctx.fillRect(centerX + 2, py + 5, 1, 1);
                ctx.fillRect(centerX - 2, py + 7, 2, 1);
                
            } else if(type === 'cake') {
                // Cake base
                ctx.fillStyle = '#DEB887';
                ctx.fillRect(px + 1, py + 4, BLOCK - 2, BLOCK - 4);
                
                // Frosting layers
                ctx.fillStyle = '#FFFFFF';
                ctx.fillRect(px + 1, py + 3, BLOCK - 2, 2);
                ctx.fillRect(px + 1, py + 1, BLOCK - 2, 2);
                
                // Cherry on top
                ctx.fillStyle = '#FF0000';
                ctx.beginPath();
                ctx.arc(centerX, py + 2, 1, 0, 2 * Math.PI);
                ctx.fill();
                
                // Cherry stem
                ctx.fillStyle = '#228B22';
                ctx.fillRect(centerX, py + 1, 1, 1);
                
                // Cake decorations
                ctx.fillStyle = '#FFB6C1';
                ctx.fillRect(px + 2, py + 5, 1, 1);
                ctx.fillRect(px + BLOCK - 3, py + 6, 1, 1);
                ctx.fillRect(centerX, py + 7, 1, 1);
            }
        } else {
            // Snake body
            ctx.fillStyle = '#00AA00'; 
            ctx.fillRect(px,py,BLOCK,BLOCK); 
            ctx.fillStyle = '#00FF00'; 
            ctx.fillRect(px+1,py+1,BLOCK-2,BLOCK-2);
        }
    }

    function addFood(){ 
        foods = []; 
        if(!canvas) return; 
        
        // Start with base foods + bonus for map expansions
        const baseFoods = 3;
        const expansionBonus = expansionsCompleted * 2; // +2 foods per expansion completed
        const totalInitialFoods = baseFoods + expansionBonus;
        
        for(let i = 0; i < totalInitialFoods; i++) {
            addSingleFood();
        }
    }
    
    function addSingleFood() {
        if(!canvas) return; 
        const cols = Math.max(1, Math.floor(currentMapWidth / BLOCK)); 
        const rows = Math.max(1, Math.floor(currentMapHeight / BLOCK)); 
        
        // Determine maximum number of foods based on snake length AND map size
        const baseMaxBySnake = Math.min(5, 3 + Math.floor((snake ? snake.length : 1) / 10));
        const mapSizeBonus = expansionsCompleted * 2; // +2 max foods per expansion
        const maxFoods = baseMaxBySnake + mapSizeBonus;
        if(foods.length >= maxFoods) return;
        
        let attempts = 0;
        while(attempts < 100){
            let fx = Math.floor(Math.random() * cols); 
            let fy = Math.floor(Math.random() * rows); 
            let coll = false;
            
            // Check collision with snake
            if(snake) {
                for(let i=0;i<snake.length;i++) {
                    if(checkBlock(fx,fy,snake[i].x,snake[i].y)) coll = true;
                }
            }
            
            // Check collision with existing foods
            for(let i=0;i<foods.length;i++) {
                if(checkBlock(fx,fy,foods[i].x,foods[i].y)) coll = true;
            }
            
            // Check collision with internal walls
            for(let i=0;i<walls.length;i++) {
                if(checkBlock(fx,fy,walls[i].x,walls[i].y)) coll = true;
            }
            
            // Check collision with lava blocks
            for(let i=0;i<lavaBlocks.length;i++) {
                if(checkBlock(fx,fy,lavaBlocks[i].x,lavaBlocks[i].y)) coll = true;
            }
            
            // Check collision with enemy snakes
            for(let e=0;e<enemies.length;e++) {
                for(let seg=0;seg<enemies[e].body.length;seg++) {
                    if(checkBlock(fx,fy,enemies[e].body[seg].x,enemies[e].body[seg].y)) coll = true;
                }
            }
            
            if(!coll) {
                const foodType = selectRandomFoodType();
                foods.push({x:fx, y:fy, type:foodType}); 
                break;
            }
            attempts++;
        }
    }
    
    function selectRandomFoodType() {
        const totalChance = Object.values(FOOD_TYPES).reduce((sum, food) => sum + food.chance, 0);
        let random = Math.random() * totalChance;
        
        for(const [type, food] of Object.entries(FOOD_TYPES)) {
            random -= food.chance;
            if(random <= 0) {
                return type;
            }
        }
        
        return 'apple'; // fallback
    }
    
    function generateInternalWalls() {
        walls = [];
        if(internal_walls === 0 || !canvas) return;
        
        const cols = Math.max(1, Math.floor(currentMapWidth / BLOCK));
        const rows = Math.max(1, Math.floor(currentMapHeight / BLOCK));
        
        // Number of wall segments based on setting
        const wallCount = internal_walls === 1 ? 3 : 6; // Few = 3, Many = 6
        
        for(let w = 0; w < wallCount; w++) {
            // Create wall segments of 2-4 blocks each
            const segmentLength = Math.floor(Math.random() * 3) + 2;
            const isHorizontal = Math.random() > 0.5;
            
            let startX, startY;
            let attempts = 0;
            
            // Find a good starting position
            do {
                if(isHorizontal) {
                    startX = Math.floor(Math.random() * (cols - segmentLength - 4)) + 2;
                    startY = Math.floor(Math.random() * (rows - 4)) + 2;
                } else {
                    startX = Math.floor(Math.random() * (cols - 4)) + 2;
                    startY = Math.floor(Math.random() * (rows - segmentLength - 4)) + 2;
                }
                attempts++;
            } while(attempts < 50 && (isNearSnakeStart(startX, startY) || isNearExistingWall(startX, startY)));
            
            // Create wall segment
            for(let i = 0; i < segmentLength; i++) {
                const wallX = isHorizontal ? startX + i : startX;
                const wallY = isHorizontal ? startY : startY + i;
                
                if(wallX >= 0 && wallX < cols && wallY >= 0 && wallY < rows) {
                    walls.push({x: wallX, y: wallY});
                }
            }
        }
    }
    
    function isNearSnakeStart(x, y) {
        // Keep walls away from snake starting position
        const snakeStartX = 16;
        const snakeStartY = 16;
        const distance = Math.abs(x - snakeStartX) + Math.abs(y - snakeStartY);
        return distance < 5;
    }
    
    function isNearExistingWall(x, y) {
        // Keep walls from overlapping
        for(let wall of walls) {
            if(Math.abs(x - wall.x) <= 1 && Math.abs(y - wall.y) <= 1) {
                return true;
            }
        }
        return false;
    }
    
    function drawWallBlock(x, y) {
        if(!ctx) return;
        const px = x * BLOCK;
        const py = y * BLOCK;
        
        // Main wall block - dark gray/brown
        ctx.fillStyle = '#696969';
        ctx.fillRect(px, py, BLOCK, BLOCK);
        
        // Top highlight
        ctx.fillStyle = '#808080';
        ctx.fillRect(px, py, BLOCK, 2);
        
        // Left highlight
        ctx.fillRect(px, py, 2, BLOCK);
        
        // Bottom shadow
        ctx.fillStyle = '#404040';
        ctx.fillRect(px, py + BLOCK - 2, BLOCK, 2);
        
        // Right shadow
        ctx.fillRect(px + BLOCK - 2, py, 2, BLOCK);
        
        // Inner detail
        ctx.fillStyle = '#555555';
        ctx.fillRect(px + 2, py + 2, BLOCK - 4, BLOCK - 4);
    }

    function generateLavaBlocks() {
        lavaBlocks = [];
        if(!canvas) return;
        
        const cols = Math.max(1, Math.floor(currentMapWidth / BLOCK));
        const rows = Math.max(1, Math.floor(currentMapHeight / BLOCK));
        
        // Calculate number of lava blocks based on map size (bigger map = more lava)
        const mapArea = cols * rows;
        const lavaCount = Math.max(3, Math.floor(mapArea / 40)); // About 2.5% of the map
        
        for(let i = 0; i < lavaCount; i++) {
            let attempts = 0;
            while(attempts < 100) {
                let lx = Math.floor(Math.random() * cols);
                let ly = Math.floor(Math.random() * rows);
                let collision = false;
                
                // Check collision with snake
                if(snake) {
                    for(let j = 0; j < snake.length; j++) {
                        if(checkBlock(lx, ly, snake[j].x, snake[j].y)) {
                            collision = true;
                            break;
                        }
                    }
                }
                
                // Check collision with foods
                for(let j = 0; j < foods.length; j++) {
                    if(checkBlock(lx, ly, foods[j].x, foods[j].y)) {
                        collision = true;
                        break;
                    }
                }
                
                // Check collision with walls
                for(let j = 0; j < walls.length; j++) {
                    if(checkBlock(lx, ly, walls[j].x, walls[j].y)) {
                        collision = true;
                        break;
                    }
                }
                
                // Check collision with existing lava blocks
                for(let j = 0; j < lavaBlocks.length; j++) {
                    if(checkBlock(lx, ly, lavaBlocks[j].x, lavaBlocks[j].y)) {
                        collision = true;
                        break;
                    }
                }
                
                // Don't place near snake starting position
                if(isNearSnakeStart(lx, ly)) {
                    collision = true;
                }
                
                if(!collision) {
                    lavaBlocks.push({x: lx, y: ly});
                    break;
                }
                
                attempts++;
            }
        }
    }

    function drawLavaBlock(x, y) {
        if(!ctx) return;
        const px = x * BLOCK;
        const py = y * BLOCK;
        
        // Main lava block - bright orange/red
        ctx.fillStyle = '#FF4500';
        ctx.fillRect(px, py, BLOCK, BLOCK);
        
        // Lava glow effect - brighter center
        ctx.fillStyle = '#FF6347';
        ctx.fillRect(px + 1, py + 1, BLOCK - 2, BLOCK - 2);
        
        // Hot center
        ctx.fillStyle = '#FFD700';
        ctx.fillRect(px + 2, py + 2, BLOCK - 4, BLOCK - 4);
        
        // Lava bubbles/spots for texture
        ctx.fillStyle = '#FF0000';
        ctx.fillRect(px + 1, py + 1, 2, 2);
        ctx.fillRect(px + BLOCK - 3, py + BLOCK - 3, 2, 2);
        
        // More hot spots
        ctx.fillStyle = '#FFFF00';
        ctx.fillRect(px + 3, py + 6, 1, 1);
        ctx.fillRect(px + 6, py + 2, 1, 1);
        ctx.fillRect(px + 7, py + 7, 1, 1);
    }

    function spawnEnemies() {
        enemies = [];
        if(!canvas) return;
        
        const cols = Math.max(1, Math.floor(currentMapWidth / BLOCK));
        const rows = Math.max(1, Math.floor(currentMapHeight / BLOCK));
        
        // Number of enemies based on map size and expansions
        const enemyCount = Math.max(1, expansionsCompleted + 1);
        
        for(let i = 0; i < enemyCount; i++) {
            let attempts = 0;
            while(attempts < 100) {
                let ex = Math.floor(Math.random() * cols);
                let ey = Math.floor(Math.random() * rows);
                let collision = false;
                
                // Check collision with player snake
                if(snake) {
                    for(let j = 0; j < snake.length; j++) {
                        if(checkBlock(ex, ey, snake[j].x, snake[j].y)) {
                            collision = true;
                            break;
                        }
                    }
                }
                
                // Check collision with other game objects
                for(let j = 0; j < foods.length; j++) {
                    if(checkBlock(ex, ey, foods[j].x, foods[j].y)) {
                        collision = true;
                        break;
                    }
                }
                
                for(let j = 0; j < walls.length; j++) {
                    if(checkBlock(ex, ey, walls[j].x, walls[j].y)) {
                        collision = true;
                        break;
                    }
                }
                
                for(let j = 0; j < lavaBlocks.length; j++) {
                    if(checkBlock(ex, ey, lavaBlocks[j].x, lavaBlocks[j].y)) {
                        collision = true;
                        break;
                    }
                }
                
                // Don't spawn too close to player or other enemies
                if(isNearSnakeStart(ex, ey) || Math.abs(ex - 16) + Math.abs(ey - 16) < 8) {
                    collision = true;
                }
                
                if(!collision) {
                    // Create enemy snake with initial length of 3
                    const enemy = {
                        body: [{x: ex, y: ey}, {x: ex, y: ey}, {x: ex, y: ey}],
                        direction: Math.floor(Math.random() * 4), // 0=up, 1=right, 2=down, 3=left
                        moveCounter: 0
                    };
                    enemies.push(enemy);
                    break;
                }
                
                attempts++;
            }
        }
    }

    function updateEnemies() {
        if(!enemiesMode || !snake || !snake.length) return;
        
        const cols = Math.max(1, Math.floor(currentMapWidth / BLOCK));
        const rows = Math.max(1, Math.floor(currentMapHeight / BLOCK));
        
        for(let e = 0; e < enemies.length; e++) {
            let enemy = enemies[e];
            
            // Move enemy every 2-3 game ticks (slower than player)
            enemy.moveCounter++;
            if(enemy.moveCounter < 3) continue;
            enemy.moveCounter = 0;
            
            // Simple AI: move towards player snake
            let playerX = snake[0].x;
            let playerY = snake[0].y;
            let enemyX = enemy.body[0].x;
            let enemyY = enemy.body[0].y;
            
            // Calculate direction to player
            let deltaX = playerX - enemyX;
            let deltaY = playerY - enemyY;
            
            // Choose direction based on larger delta
            let newDir = enemy.direction;
            if(Math.abs(deltaX) > Math.abs(deltaY)) {
                newDir = deltaX > 0 ? 1 : 3; // Right or Left
            } else {
                newDir = deltaY > 0 ? 2 : 0; // Down or Up
            }
            
            // Calculate new head position
            let newX = enemyX;
            let newY = enemyY;
            
            switch(newDir) {
                case 0: newY--; break; // Up
                case 1: newX++; break; // Right
                case 2: newY++; break; // Down
                case 3: newX--; break; // Left
            }
            
            // Handle wall collision (wrap around if walls are off)
            if(wall === 1) {
                if(newX < 0 || newX >= cols || newY < 0 || newY >= rows) {
                    // Bounce off walls by choosing random direction
                    newDir = Math.floor(Math.random() * 4);
                    newX = enemyX;
                    newY = enemyY;
                    switch(newDir) {
                        case 0: newY--; break;
                        case 1: newX++; break;
                        case 2: newY++; break;
                        case 3: newX--; break;
                    }
                    // If still hitting wall, don't move
                    if(newX < 0 || newX >= cols || newY < 0 || newY >= rows) {
                        continue;
                    }
                }
            } else {
                if(newX < 0) newX = cols - 1;
                if(newX >= cols) newX = 0;
                if(newY < 0) newY = rows - 1;
                if(newY >= rows) newY = 0;
            }
            
            // Check collision with walls and obstacles
            let collision = false;
            for(let w = 0; w < walls.length; w++) {
                if(checkBlock(newX, newY, walls[w].x, walls[w].y)) {
                    collision = true;
                    break;
                }
            }
            
            // If collision, try random direction
            if(collision) {
                newDir = Math.floor(Math.random() * 4);
                continue;
            }
            
            // Move enemy
            enemy.direction = newDir;
            enemy.body.pop(); // Remove tail
            enemy.body.unshift({x: newX, y: newY}); // Add new head
        }
    }

    function drawEnemySnake(enemy) {
        if(!ctx || !enemy.body) return;
        
        for(let i = 0; i < enemy.body.length; i++) {
            const segment = enemy.body[i];
            const px = segment.x * BLOCK;
            const py = segment.y * BLOCK;
            
            // Draw red enemy snake
            if(i === 0) {
                // Enemy head - darker red
                ctx.fillStyle = '#8B0000';
                ctx.fillRect(px, py, BLOCK, BLOCK);
                
                // Eyes
                ctx.fillStyle = '#FFFF00';
                ctx.fillRect(px + 2, py + 2, 2, 2);
                ctx.fillRect(px + 6, py + 2, 2, 2);
            } else {
                // Enemy body - bright red
                ctx.fillStyle = '#FF0000';
                ctx.fillRect(px, py, BLOCK, BLOCK);
                
                // Body highlight
                ctx.fillStyle = '#FF4444';
                ctx.fillRect(px + 1, py + 1, BLOCK - 2, BLOCK - 2);
            }
        }
    }

    function checkBlock(x,y,_x,_y){
        return x===_x && y===_y;
    }

    function updateStats(score_val){ 
        if(ele_lives) ele_lives.innerText = String(lives); 
        if(ele_score) ele_score.innerText = String(score_val); 
        if(ele_snake_length) ele_snake_length.innerText = String(snake?snake.length:0); 
        game_level = Math.floor(score_val/5)+1; 
        if(ele_game_level) ele_game_level.innerText = String(game_level); 
        
        // Update map size display
        if(ele_map_size) ele_map_size.innerText = `${currentMapWidth}x${currentMapHeight}`;
        
        // Update next expansion display
        if(ele_next_expansion) {
            if(expansionsCompleted >= expansionThresholds.length) {
                ele_next_expansion.innerText = 'MAX SIZE';
            } else {
                const nextThreshold = expansionThresholds[expansionsCompleted];
                ele_next_expansion.innerText = `Length ${nextThreshold}`;
            }
        }
        
        if(score_val>high_score){ 
            high_score = score_val; 
            try{ 
                localStorage.setItem('snake_high_score', String(high_score)); 
            }catch(e){} 
            if(ele_high_score) ele_high_score.innerText = String(high_score); 
            showAchievement('NEW HIGH SCORE!'); 
        } else if(ele_high_score) {
            ele_high_score.innerText = String(high_score); 
        }
    }

    function showAchievement(t){ 
        if(ele_achievement_text) ele_achievement_text.innerText = t; 
        if(ele_achievement_banner) ele_achievement_banner.style.display='block'; 
        setTimeout(()=>{ 
            if(ele_achievement_banner) ele_achievement_banner.style.display='none'; 
        },3000); 
    }

    function setSnakeSpeed(v){ 
        snake_speed = parseInt(v) || 75; 
    }
    
    function setWall(v){ 
        wall = parseInt(v) || 0; 
        const s = $id('snake_canvas'); 
        if(s) s.style.borderColor = (wall===0)?'#606060':'#FFFFFF'; 
    }
    
    function computeLives(){
        if(challengeMode) {
            lives = 1; 
        } else { 
            let sp = parseInt(snake_speed); 
            if(sp===300) lives=5; 
            else if(sp===120) lives=4; 
            else if(sp===75) lives=3; 
            else if(sp===35) lives=2; 
            else lives=1; 
        }
        if(ele_lives) ele_lives.innerText = String(lives);
    }

    // Initialize when DOM is ready
    if(document.readyState === 'loading'){
        document.addEventListener('DOMContentLoaded', init);
    } else {
        setTimeout(init, 100);
    }

})();
</script>
<noscript style="color:orange; font-weight:bold;">JavaScript is disabled or the snake script failed to load — controls will not work.</noscript>

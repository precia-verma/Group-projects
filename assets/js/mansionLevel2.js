    import GameEnvBackground from './GameEngine/<path>.js'
    import AnimatedPlayer from './GameEngine/<path>.js'
    import Platform from './GameEngine/<path>.js'
    import Level from './GameEngine/<path>.js'
    
    // Create the game environment with a spooky mansion background
    const gameEnv = new GameEnvBackground('world', 'images/platformer/backgrounds/spookyforestforgame.png'); 
    const player = new AnimatedPlayer(50, 300, 'images/platformer/sprites/gravestone_1.png', 64, 64);
    
    // Define platforms for the mansion level
    const platforms = [
        new Platform(0, 400, 800, 20), // Ground platform
        new Platform(150, 300, 100, 20),
        new Platform(300, 250, 100, 20),
        new Platform(450, 200, 100, 20),
        new Platform(600, 150, 100, 20),
    ];
    
    // Create the mansion level
    const mansionLevel = new Level(gameEnv, player, platforms);
    
    // Start the game loop
    mansionLevel.start();       


    export default mansionLevel;    
    

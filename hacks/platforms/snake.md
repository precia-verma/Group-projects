// Snake game Helper
'use strict';

function checkBlock(x,y,_x,_y){
    return x===_x && y===_y;
}

function computeLivesFrom(speedValue, challengeMode){
    if(challengeMode) return 1;
    const sp = parseInt(speedValue, 10);
    if(sp===300) return 5;
    if(sp===120) return 4;
    if(sp===75) return 3;
    if(sp===35) return 2;
    return 1;
}

function mapSizeForLength(len){
    if(len>=30) return 640;
    if(len>=20) return 480;
    if(len>=10) return 400;
    return 320;
}

// expose in Node (for tests) and in browser
if(typeof module !== 'undefined' && module.exports){
    module.exports = { checkBlock, computeLivesFrom, mapSizeForLength };
}
if(typeof window !== 'undefined'){
    window._snake_helpers = window._snake_helpers || {};
    window._snake_helpers.checkBlock = checkBlock;
    window._snake_helpers.computeLivesFrom = computeLivesFrom;
    window._snake_helpers.mapSizeForLength = mapSizeForLength;
}

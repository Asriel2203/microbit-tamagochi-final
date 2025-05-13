controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    playerHand = sprites.create(img`
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . d d b d . . . . 
        . . . . . . . d d b d d b d . . 
        . . . . . . . d b d d b d d . . 
        . . . . . . d d d d b d d b . . 
        . . . 1 1 b b d d d d d b d b . 
        . 1 1 1 5 5 b b d d d b d d b . 
        1 1 5 5 5 5 5 b b d d d d b . . 
        5 5 5 5 5 5 5 5 b b d d d b . . 
        5 5 5 5 5 5 5 5 b . b b b . . . 
        5 5 5 5 5 5 5 5 b . . . . . . . 
        5 5 5 5 5 5 5 5 b . . . . . . . 
        5 5 5 5 5 5 b b b . . . . . . . 
        5 5 5 5 b b b . . . . . . . . . 
        5 5 5 5 b . . . . . . . . . . . 
        `, SpriteKind.Enemy)
    playerHand.setPosition(16, randint(10, 100))
    projectile = sprites.createProjectileFromSprite(img`
        . . . . . . . e c 7 . . . . . . 
        . . . . e e e c 7 7 e e . . . . 
        . . c e e e e c 7 e 2 2 e e . . 
        . c e e e e e c 6 e e 2 2 2 e . 
        . c e e e 2 e c c 2 4 5 4 2 e . 
        c e e e 2 2 2 2 2 2 4 5 5 2 2 e 
        c e e 2 2 2 2 2 2 2 2 4 4 2 2 e 
        c e e 2 2 2 2 2 2 2 2 2 2 2 2 e 
        c e e 2 2 2 2 2 2 2 2 2 2 2 2 e 
        c e e 2 2 2 2 2 2 2 2 2 2 2 2 e 
        c e e 2 2 2 2 2 2 2 2 2 2 4 2 e 
        . e e e 2 2 2 2 2 2 2 2 2 4 e . 
        . 2 e e 2 2 2 2 2 2 2 2 4 2 e . 
        . . 2 e e 2 2 2 2 2 4 4 2 e . . 
        . . . 2 2 e e 4 4 4 2 e e . . . 
        . . . . . 2 2 e e e e . . . . . 
        `, playerHand, 50, 0)
    pause(2000)
    sprites.destroy(playerHand)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Player, function (sprite, otherSprite) {
    sprites.destroy(projectile)
    determine_pet_full()
    statusbars.getStatusBarAttachedTo(StatusBarKind.Health, pet_egg).value += 2
})
statusbars.onStatusReached(StatusBarKind.Health, statusbars.StatusComparison.LTE, statusbars.ComparisonType.Percentage, 50, function (status) {
    determine_pet_call()
    pause(1000)
})
statusbars.onZero(StatusBarKind.Health, function (status) {
    sprites.destroy(pet_egg)
    pet_egg = sprites.create(img`
        ........................
        ........................
        ........................
        ........................
        ..........ffff..........
        ........ff1111ff........
        .......fb111111bf.......
        .......f11111111f.......
        ......fd11111111df......
        ......fd11111111df......
        ......fddd1111dddf......
        ......fbdbfddfbdbf......
        ......fcdcf11fcdcf......
        .......fb111111bf.......
        ......fffcdb1bdffff.....
        ....fc111cbfbfc111cf....
        ....f1b1b1ffff1b1b1f....
        ....fbfbffffffbfbfbf....
        .........ffffff.........
        ...........fff..........
        ........................
        ........................
        ........................
        ........................
        `, SpriteKind.Player)
    animation.runMovementAnimation(
    pet_egg,
    animation.animationPresets(animation.easeUp),
    5000,
    false
    )
    music.play(music.stringPlayable("A - G F E D C D ", 120), music.PlaybackMode.UntilDone)
    game.splash("Oh no!", "Your pet died!")
    game.splash("Want a", "second chance?")
    game.reset()
})
function determine_pet_call () {
    if (pet_int == 0) {
        animation.runImageAnimation(
        pet_egg,
        [img`
            . . . . . . . . . b 5 b . . . . 
            . . . . . . . . . b 5 b . . . . 
            . . . . . . b b b b b b . . . . 
            . . . . . b b 5 5 5 5 5 b . . . 
            . . . . b b 5 b c 5 5 d 4 c . . 
            . b b b b 5 5 5 b f d d 4 4 4 b 
            . b d 5 b 5 5 b c b 4 4 4 4 b . 
            . . b 5 5 b 5 5 5 4 4 4 4 b . . 
            . . b d 5 5 b 5 5 5 5 5 5 b . . 
            . b d b 5 5 5 d 5 5 5 5 5 5 b . 
            b d d c d 5 5 b 5 5 5 5 5 5 b . 
            c d d d c c b 5 5 5 5 5 5 5 b . 
            c b d d d d d 5 5 5 5 5 5 5 b . 
            . c d d d d d d 5 5 5 5 5 d b . 
            . . c b d d d d d 5 5 5 b b . . 
            . . . c c c c c c c c b b . . . 
            `,img`
            . . . . . . . . . . b 5 b . . . 
            . . . . . . . . . b 5 b . . . . 
            . . . . . . b b b b b b . . . . 
            . . . . . b b 5 5 5 5 5 b . . . 
            . . . . b b 5 d 1 f 5 5 d f . . 
            . . . . b 5 5 1 f f 5 d 4 c . . 
            . . . . b 5 5 d f b d d 4 4 . . 
            . b b b d 5 5 5 5 5 4 4 4 4 4 b 
            b d d d b b d 5 5 4 4 4 4 4 b . 
            b b d 5 5 5 b 5 5 5 5 5 5 b . . 
            c d c 5 5 5 5 d 5 5 5 5 5 5 b . 
            c b d c d 5 5 b 5 5 5 5 5 5 b . 
            . c d d c c b d 5 5 5 5 5 d b . 
            . . c b d d d d d 5 5 5 b b . . 
            . . . c c c c c c c c b b . . . 
            . . . . . . . . . . . . . . . . 
            `,img`
            . . . . . . . . . . b 5 b . . . 
            . . . . . . . . . b 5 b . . . . 
            . . . . . . b b b b b b . . . . 
            . . . . . b b 5 5 5 5 5 b . . . 
            . . . . b b 5 d 1 f 5 d 4 c . . 
            . . . . b 5 5 1 f f d d 4 4 4 b 
            . . . . b 5 5 d f b 4 4 4 4 b . 
            . . . b d 5 5 5 5 4 4 4 4 b . . 
            . b b d d d 5 5 5 5 5 5 5 b . . 
            b d d d b b b 5 5 5 5 5 5 5 b . 
            c d d b 5 5 d c 5 5 5 5 5 5 b . 
            c b b d 5 d c d 5 5 5 5 5 5 b . 
            c b 5 5 b c d d 5 5 5 5 5 5 b . 
            b b c c c d d d 5 5 5 5 5 d b . 
            . . . . c c d d d 5 5 5 b b . . 
            . . . . . . c c c c c b b . . . 
            `],
        5000,
        true
        )
        music.play(music.stringPlayable("- A - A - A - A ", 120), music.PlaybackMode.UntilDone)
    } else if (pet_int == 1) {
        animation.runImageAnimation(
        pet_egg,
        [img`
            . . . . . c c c c c c c . . . . 
            . . . . c 6 7 7 7 7 7 6 c . . . 
            . . . c 7 c 6 6 6 6 c 7 6 c . . 
            . . c 6 7 6 f 6 6 f 6 7 7 c . . 
            . . c 7 7 7 7 7 7 7 7 7 7 c . . 
            . . f 7 8 1 f f 1 6 7 7 7 f . . 
            . . f 6 f 1 f f 1 f 7 7 7 f . . 
            . . . f f 2 2 2 2 f 7 7 6 f . . 
            . . c c f 2 2 2 2 7 7 6 f c . . 
            . c 7 7 7 7 7 7 7 7 c c 7 7 c . 
            c 7 1 1 1 7 7 7 7 f c 6 7 7 7 c 
            f 1 1 1 1 1 7 6 f c c 6 6 6 c c 
            f 1 1 1 1 1 1 6 6 c 6 6 6 c . . 
            f 6 1 1 1 1 1 6 6 6 6 6 6 c . . 
            . f 6 1 1 1 1 1 6 6 6 6 c . . . 
            . . f f c c c c c c c c . . . . 
            `,img`
            . . . . . . c c c c c c c . . . 
            . . . . . c f f 6 6 f f 7 c . . 
            . . . . c 7 6 6 6 6 6 6 7 6 c . 
            . . . c 7 7 7 7 7 7 7 7 7 7 c . 
            . . . c 7 8 1 f f 1 6 7 7 7 c . 
            . . . f 6 f 1 f f 1 f 7 7 7 f . 
            . . . f 6 f 2 2 2 2 f 7 7 7 f . 
            . . c c 6 f 2 2 2 2 f 7 7 6 f . 
            . c 7 7 7 7 2 2 2 2 7 7 f c . . 
            c 7 1 1 1 7 7 7 7 7 c c 7 7 c . 
            f 1 1 1 1 1 7 7 7 f c 6 7 7 7 c 
            f 1 1 1 1 1 1 6 f c c 6 6 6 c c 
            f 6 1 1 1 1 1 6 6 c 6 6 6 c . . 
            f 6 1 1 1 1 1 6 6 6 6 6 6 c . . 
            . f 6 1 1 1 1 6 6 6 6 6 c . . . 
            . . f f c c c c c c c c . . . . 
            `,img`
            . . . . . . c c c c c c c . . . 
            . . . . . c f f 6 6 f f 7 c . . 
            . . . . c 7 6 6 6 6 6 6 7 6 c . 
            . . . c 7 7 7 7 7 7 7 7 7 7 c . 
            . . . c 7 8 1 f f 1 6 7 7 7 c . 
            . . . f 6 f 1 f f 1 f 7 7 7 f . 
            . . . f 6 f 2 2 2 2 f 7 7 7 f . 
            . . c c 6 f 2 2 2 2 f 7 7 6 f . 
            . c 7 7 7 7 2 2 2 2 7 7 f c . . 
            c 7 1 1 1 7 7 7 7 7 c c 7 7 c . 
            f 1 1 1 1 1 7 7 7 f c 6 7 7 7 c 
            f 1 1 1 1 1 1 6 f c c 6 6 6 c c 
            f 6 1 1 1 1 1 6 6 c 6 6 6 c . . 
            f 6 1 1 1 1 1 6 6 6 6 6 6 c . . 
            . f 6 1 1 1 1 6 6 6 6 6 c . . . 
            . . f f c c c c c c c c . . . . 
            `,img`
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . c c c c c 
            . . . . . . . . . c c 7 7 7 6 c 
            . . . . . . . . c c 7 7 7 c c . 
            . . . . . . . . c 6 7 7 c . . . 
            . . . . . . . . c 6 6 6 c . . . 
            . . . c c c c c c 6 6 6 c c . . 
            . . c 6 7 7 7 7 6 c c 6 6 6 c . 
            . c 7 7 7 7 7 7 7 7 c 6 6 6 c c 
            c 6 7 7 7 7 7 7 7 7 6 c 6 6 6 c 
            c 7 c 6 6 6 6 c 7 7 7 c 6 6 6 c 
            f 7 c c 6 6 c c 7 7 7 f 6 6 6 c 
            f 7 6 f 6 6 f 6 7 7 7 f 6 6 6 c 
            . c 1 c f f 1 c 7 6 f 6 6 c c . 
            . c c c c c c c c c c c c . . . 
            `,img`
            . . . . . . . . . . . c c c c c 
            . . . . . . . . . c c 7 7 7 6 c 
            . . . . . . . . c c 7 7 7 c c . 
            . . . . . . . . c 6 7 7 c . . . 
            . . . . . . . . c 6 6 6 c . . . 
            . . . . . . . . c 6 6 6 c c . . 
            . . . c c c c c c c 6 6 6 c c . 
            . . c 6 7 7 7 7 6 c c 6 6 6 c . 
            . c 7 7 7 7 7 7 7 7 c 6 6 6 c c 
            c 6 7 7 7 7 7 7 7 7 6 c 6 6 6 c 
            c 7 c 6 6 6 6 c 7 7 7 c 6 6 6 c 
            f 7 c c 6 6 c c 7 7 7 f 6 6 6 c 
            f 7 6 f 6 6 f 6 7 7 7 f 6 6 6 c 
            . f 7 7 7 7 7 7 7 7 6 f 6 6 c . 
            . c 1 c f f 1 c 7 6 f 6 6 c c . 
            . c c c c c c c c c c c c . . . 
            `,img`
            . . . . . . . . . . . c c c c c 
            . . . . . . . . . c c 7 7 7 6 c 
            . . . . . . . . c c 7 7 7 c c . 
            . . . . . . . . c 6 7 7 c . . . 
            . . . . . . . . c 6 6 6 c . . . 
            . . . . . . . . c 6 6 6 c c . . 
            . . . c c c c c c c 6 6 6 c c . 
            . . c 6 7 7 7 7 6 c c 6 6 6 c . 
            . c 7 7 7 7 7 7 7 7 c 6 6 6 c c 
            c 6 7 7 7 7 7 7 7 7 6 c 6 6 6 c 
            c 7 c 6 6 6 6 c 7 7 7 c 6 6 6 c 
            f 7 c c 6 6 c c 7 7 7 f 6 6 6 c 
            f 7 6 f 6 6 f 6 7 7 7 f 6 6 6 c 
            . f 7 7 7 7 7 7 7 7 6 f 6 6 c . 
            . c 1 c f f 1 c 7 6 f 6 6 c c . 
            . c c c c c c c c c c c c . . . 
            `],
        500,
        true
        )
        music.play(music.stringPlayable("- A - A - A - A ", 120), music.PlaybackMode.UntilDone)
    } else if (pet_int == 2) {
        animation.runImageAnimation(
        pet_egg,
        [img`
            ........................
            ........................
            ..........ccc...........
            .........cccc...........
            .....ccccccc..ccc.......
            ...cc555555cccccc.......
            ..c5555555555bcc........
            .c555555555555b..cc.....
            c555551ff555555bccc.....
            c55d55ff55555555bc......
            c5555555555555555b......
            .cbb31bb5555dd555b.cc...
            .c5333b555ddddd55dccc...
            .c533b55ddddddddddb.....
            .c5555dddbb55bdddddccc..
            ..ccccbbbb555bdddddccc..
            ...cdcbc5555bddddddcc...
            ....ccbc55bc5ddddddbcccc
            .....cbbcc5555dddddddddc
            .....ccbbb555ddbddddddc.
            .....cdcbc55ddbbbdddcc..
            ...ccdddccddddbcbbcc....
            ...ccccccd555ddccc......
            ........cccccccc........
            `,img`
            ............ccc.........
            .......cccccccc.........
            .....cc55555cc..cc......
            ....c555555555cccc......
            ...c55555555555bcc......
            ..c555551ff55555b..cc...
            ..c55d55ff5555555bccc...
            ..c55555555d55555bcc....
            ..c5555d5555d55555b.....
            ..cbbbb55555ddd555b.cc..
            ..c555d5555ddddd55dccc..
            ...c555dbbbdddbd5ddcc...
            ....cccbbbbb555bdddb....
            ....cbbbbbbc555bdddccc..
            ...cbbbbbbc555bddddcc...
            ...cbbbbbc555bdddddc....
            ..ccbbbbbc55bddddddcc...
            ..ccbbbbbbcb55dddddbcc..
            ...cbbbbbb5555ddddddddcc
            ....cbbbbb555ddbdddddddc
            ....cccbbc55ddbbbddddcc.
            ...ccdddccddddbcbbccc...
            ...ccccccd555ddccc......
            ........cccccccc........
            `,img`
            .............ccc........
            ........cccccccc........
            ......cc55555cc..cc.....
            .....c555555555cccc.....
            ....c55555555555bcc.....
            ...c555555ccb5555b.cc...
            ...c55d55c55555555bcc...
            ...c55555555dd5555bc....
            ...c5555d5555dd5555.....
            ...cbbbd555555dd555.cc..
            ...c555d555555ddd55ccc..
            ....c555d5555ddbd5dcc...
            ....cccbbbbb555bdddb....
            ...cbbbbbbbc555bdddccc..
            ..cbbbbbbbc555bddddcc...
            ..cbbbbbbc555bdddddc....
            .ccbbbbbbc55bddddddcc...
            .ccbbbbbbbcb55dddddbc...
            ..cbbbbbbb5555ddddddbc..
            ...cbbbbbb555ddbddddddc.
            ....cccbbc55ddbbbddddddc
            ...ccdddccddddbcbbcccccc
            ...ccccccd555ddccc......
            ........cccccccc........
            `,img`
            ........................
            ........................
            ........................
            ..........ccc...........
            .........cccc...........
            .....ccccccc..ccc.......
            ...cc555555cccccc.......
            ..c5555555555bcc........
            .c555555555555b..cc.....
            c555555ccb55555bccc.....
            c55d55c555555555bc......
            c5555555555555555b......
            .cbbb1bb5555dd555b.cc...
            .c533bbbb5ddddd55dcc....
            .c533bbbb5ddddddddbcc...
            .c533bbb55dddddddddcccc.
            .c5333bb5bb55bdddddcccdc
            .c5333b5bb555bddddddbddc
            .c53335b5555bddddddddddc
            ..c5555c55bb55dbddddddcc
            ...cccbccc55ddbbbddddcc.
            ....cdddccddddbcbbbcc...
            ....cccccd555ddcccc.....
            ........cccccccc........
            `,img`
            ........................
            ........................
            ........................
            ..........ccc...........
            .........cccc...........
            .....ccccccc..ccc.......
            ...cc555555cccccc.......
            ..c5555555555bcc........
            .c555555555555b..cc.....
            c555555ccb55555bccc.....
            c55d55c555555555bc......
            c5555555555555555b......
            .cbbb1bb5555dd555b.cc...
            .c533bbbb5ddddd55dcc....
            .c533bbbb5ddddddddbcc...
            .c5333bb55dddddddddcccc.
            .c5333b55bb55bdddddcccdc
            .c533355bb555bddddddbddc
            ..c5555b5555bddddddddddc
            ...cccbc55bb55dbddddddcc
            .....cbbcc55ddbbbddddcc.
            ....cdddccddddbcbbbcc...
            ....cccccd555ddcccc.....
            ........cccccccc........
            `,img`
            ........................
            ........................
            ........................
            ..........ccc...........
            .........cccc...........
            .....ccccccc..ccc.......
            ...cc555555cccccc.......
            ..c5555555555bcc........
            .c555555555555b..cc.....
            c555555ccb55555bccc.....
            c55d55c555555555bc......
            c5555555555555555b......
            .cbbb1bb5555dd555b.cc...
            .c533bbb55ddddd55dcc....
            .c5333bb5dddddddddbcc...
            .c5333b55ddddddddddcccc.
            .c533355dbb55bdddddcccdc
            ..c55555bb555bddddddbddc
            ...cccbb5555bddddddddddc
            .....cbc55bb55dbddddddcc
            .....cdbcc55ddbbbddddcc.
            ....cdddccddddbcbbbcc...
            ....cccccd555ddcccc.....
            ........cccccccc........
            `],
        500,
        true
        )
        music.play(music.stringPlayable("- A - A - A - A ", 120), music.PlaybackMode.UntilDone)
    }
}
function determine_pet_idle () {
    if (pet_int == 0) {
        animation.runImageAnimation(
        pet_egg,
        [img`
            . . . . . . . . . . . . . . . . 
            . . . b 5 b . . . . . . . . . . 
            . . . . b 5 b . . . . . . . . . 
            . . . . b b b b b b . . . . . . 
            . . . b 5 5 5 5 5 b b . . . . . 
            . . b 5 5 5 5 5 5 5 b b b b b . 
            . . b 5 5 5 5 5 5 5 5 b 5 d b . 
            . . f 4 d 5 f 1 d 5 b 5 5 b . . 
            . . c 4 4 5 f f 1 b 5 5 d b . . 
            b 4 4 4 4 4 b f d 5 5 5 b d b b 
            . b 4 4 4 4 4 5 b 5 5 d c d d b 
            . b 5 5 5 5 5 5 5 b c c d d d c 
            . b 5 5 5 5 5 5 5 d d d d d b c 
            . b d 5 5 5 5 5 d d d d d d c . 
            . . b b 5 5 5 d d d d d b c . . 
            . . . b b c c c c c c c c . . . 
            `,img`
            . . . b 5 b . . . . . . . . . . 
            . . . . b 5 b . . . . . . . . . 
            . . . . . c b . . . . . . . . . 
            . . . . b b b b b b . . . . . . 
            . . . b 5 5 5 5 5 b b . . . . . 
            . . f d 5 5 f 1 d 5 b b . . . . 
            . . c 4 d 5 f f 1 5 5 b . . . . 
            . . 4 4 d d b f d 5 5 b . . . . 
            b 4 4 4 4 4 5 5 5 d b b d d d b 
            . b 4 4 4 4 4 5 5 b 5 5 5 d b b 
            . . b 5 5 5 5 5 d 5 5 5 5 c d b 
            . b 5 5 5 5 5 5 b 5 5 d c d d c 
            . b 5 5 5 5 5 5 5 b c c d d b c 
            . b d 5 5 5 5 5 d d d d d d c . 
            . . b b 5 5 5 d d d d d b c . . 
            . . . b b c c c c c c c c . . . 
            `,img`
            . . . b 5 b . . . . . . . . . . 
            . . . . b 5 b . . . . . . . . . 
            . . . . b b b b b b . . . . . . 
            . . . b 5 5 5 5 5 b b . . . . . 
            . . c 4 d 5 f 1 d 5 b b . . . . 
            b 4 4 4 d d f f 1 5 5 b . . . . 
            . b 4 4 4 4 b f d 5 5 b . . . . 
            . . b 4 4 4 4 5 5 5 5 d b . . . 
            . . b 5 5 5 5 5 5 5 5 d d b . . 
            . b 5 5 5 5 5 5 5 5 d d d d b . 
            . b 5 5 5 5 5 5 5 b b b d d d b 
            . b 5 5 5 5 5 5 c d 5 5 b d d c 
            . b 5 5 5 5 5 5 d c d 5 d b b c 
            . b d 5 5 5 5 5 d d c b 5 5 b . 
            . . b b 5 5 5 d d d d c c c b b 
            . . . b b c c c c c c c c . . . 
            `,img`
            . . . b 5 b . . . . . . . . . . 
            . . . . b 5 b . . . . . . . . . 
            . . . . b b b b b b . . . . . . 
            . . . b 5 5 5 5 5 b b . . . . . 
            . . c 4 d 5 f 1 d 5 b b . . . . 
            b 4 4 4 d d f f 1 5 5 b . . . . 
            . b 4 4 4 4 b f d 5 5 b . . . . 
            . . b 4 4 4 4 5 5 5 5 d b . . . 
            . . b 5 5 5 5 5 5 5 d d d b b . 
            . b 5 5 5 5 5 5 5 b b b d d d b 
            . b 5 5 5 5 5 5 c d 5 5 b d d c 
            . b 5 5 5 5 5 5 d c d 5 d b b c 
            . b 5 5 5 5 5 5 d d c b 5 5 b c 
            . b d 5 5 5 5 5 d d d c c c b b 
            . . b b 5 5 5 d d d c c . . . . 
            . . . b b c c c c c . . . . . . 
            `,img`
            . . . b 5 b . . . . . . . . . . 
            . . . . b 5 b . . . . . . . . . 
            . . . . b b b b b b . . . . . . 
            . . . b 5 5 5 5 5 b b . . . . . 
            . . f d 5 5 f 1 d 5 b b . . . . 
            . . c 4 d 5 f f 1 5 5 b . . . . 
            . . 4 4 d d b f d 5 5 b . . . . 
            b 4 4 4 4 4 5 5 5 5 5 d b b b . 
            . b 4 4 4 4 4 5 5 d b b d d d b 
            . . b 5 5 5 5 5 5 b 5 5 5 d b b 
            . b 5 5 5 5 5 5 d 5 5 5 5 c d c 
            . b 5 5 5 5 5 5 b 5 5 d c d b c 
            . b d 5 5 5 5 5 d b c c d d c . 
            . . b b 5 5 5 d d d d d b c . . 
            . . . b b c c c c c c c c . . . 
            . . . . . . . . . . . . . . . . 
            `],
        500,
        true
        )
    } else if (pet_int == 1) {
        animation.runImageAnimation(
        pet_egg,
        [img`
            . . . . . . c c c c c c . . . . 
            . . . . . c 6 7 7 7 7 6 c . . . 
            . . . . c 7 7 7 7 7 7 7 7 c . . 
            . . . c 6 7 7 7 7 7 7 7 7 6 c . 
            . . . c 7 7 7 c 6 6 6 6 c 7 c . 
            . . . f 7 7 7 6 f 6 6 f 6 7 f . 
            . . . f 7 7 7 7 7 7 7 7 7 7 f . 
            . . c f 6 7 7 c 6 7 7 7 7 f . . 
            . c 7 7 f 6 7 7 c c c c f . . . 
            c 7 7 7 7 f c 6 7 7 7 2 7 c . . 
            c c 6 7 7 6 c f c 7 7 2 7 7 c . 
            . . c 6 6 6 c c f 6 7 1 1 1 1 c 
            . . f 6 6 6 6 c 6 6 1 1 1 1 1 f 
            . . f c 6 6 6 6 6 1 1 1 1 1 6 f 
            . . . f 6 6 6 1 1 1 1 1 1 6 f . 
            . . . . f c c c c c c c c c . . 
            `,img`
            . . . . . . . c c c c c c . . . 
            . . . . . . c 6 7 7 7 7 6 c . . 
            . . . . . c 7 7 7 7 7 7 7 7 c . 
            . . . . c 6 7 7 7 7 7 7 7 7 6 c 
            . . . . c 7 7 7 c 6 6 6 6 c 7 c 
            . . . . f 7 7 7 6 f 6 6 f 6 7 f 
            . . . . f 7 7 7 7 7 7 7 7 7 7 f 
            . . . . f 6 7 7 c 6 7 7 7 7 f . 
            . . c c c f 6 7 7 c c c c f . . 
            . c 7 7 7 c c f 7 7 7 2 6 c . . 
            c 7 7 7 7 6 f c 7 7 2 7 7 6 c . 
            c c c 6 6 6 c 6 6 7 1 1 1 1 c . 
            . . c 6 6 6 6 6 6 1 1 1 1 1 c . 
            . . c 6 6 6 6 6 1 1 1 1 1 6 c . 
            . . c c 6 6 7 1 1 1 1 1 6 c . . 
            . . . c c c c c c c c c c . . . 
            `],
        500,
        true
        )
    } else if (pet_int == 2) {
        animation.runImageAnimation(
        pet_egg,
        [img`
            . . . . . . . . . . . . . . . . 
            . . . . c c c c . . . . . . . . 
            . . c c 5 5 5 5 c c . . . . . . 
            . c 5 5 5 5 5 5 5 5 c . . . . . 
            c 5 5 5 5 5 1 f 5 5 5 c . . . . 
            c 5 5 5 5 5 f f 5 5 5 5 c . . . 
            c 5 5 5 5 5 5 5 5 5 5 5 c . . . 
            c c b b 1 b 5 5 5 5 5 5 d c . . 
            c 5 3 3 3 5 5 5 5 5 d d d c . . 
            . b 5 5 5 5 5 5 5 5 d d d c . . 
            . . c b b c 5 5 b d d d d c c . 
            . c b b c 5 5 b b d d d d c d c 
            . c c c c c c d d d d d d d d c 
            . . . c c c c d 5 5 b d d d c . 
            . . c c c c c b 5 5 b c c c . . 
            . . c b b b c d 5 5 b c . . . . 
            `,img`
            . . . . c c c c c . . . . . . . 
            . . c c 5 5 5 5 5 c . . . . . . 
            . c 5 5 5 5 1 f 5 5 c . . . . . 
            c 5 5 5 5 5 f f 5 5 5 c . . . . 
            c 5 5 5 5 5 5 5 5 5 5 5 c . . . 
            c c b b 1 b 5 5 5 5 5 5 c . . . 
            c 5 3 3 3 5 5 5 5 5 5 5 d c . . 
            c 5 3 3 3 5 5 5 5 5 d d d c . . 
            . c 5 5 5 5 b 5 5 5 d d d c . . 
            . . c b b c 5 5 b d d d d c . . 
            . c b b c 5 5 b b d d d d c c c 
            . c c c c c c d d d d d d d d c 
            . . . . c c c b 5 5 b d d d c . 
            . . . . . c d 5 5 b b c c c . . 
            . . . . c c c c c c c . . . . . 
            . . . . c b b b c . . . . . . . 
            `,img`
            . . . . c c c c c . . . . . . . 
            . . c c 5 5 5 5 5 c . . . . . . 
            . c 5 5 5 5 1 f 5 5 c . . . . . 
            c 5 5 5 5 5 f f 5 5 5 c . . . . 
            c 5 5 5 5 5 5 5 5 5 5 5 c . . . 
            c c b b 1 b 5 5 5 5 5 5 c . . . 
            c 5 3 3 3 5 5 5 5 5 5 5 d c . . 
            c 5 5 5 5 5 5 5 5 5 d d d c . . 
            . c 5 5 5 5 b 5 5 5 d d d c . . 
            . . c b b c 5 5 b d d d d c . . 
            . c b b c 5 5 b b d d d d c c c 
            . c c c c c c d d d d d d d d c 
            . . . . c c b 5 5 b d d d c c . 
            . . . . c d 5 5 b b c c c . . . 
            . . . . c c c c c c c . . . . . 
            . . . . c b b b c . . . . . . . 
            `,img`
            . . . . c c c c c . . . . . . . 
            . . c c 5 5 5 5 5 c . . . . . . 
            . c 5 5 5 5 1 f 5 5 c . . . . . 
            c 5 5 5 5 5 f f 5 5 5 c . . . . 
            c 5 5 5 5 5 5 5 5 5 5 5 c . . . 
            c c b b 1 b 5 5 5 5 5 5 c . . . 
            c 5 3 3 3 5 5 5 5 5 5 5 d c . . 
            c 5 5 5 5 5 5 5 5 5 d d d c . . 
            . c 5 5 5 5 b 5 5 5 d d d c . . 
            . . c b b c 5 5 b d d d d c . . 
            . c b b c 5 5 b b d d d d c c . 
            . c c c c c b b d d d d d d c c 
            . . . c c 5 5 b 5 5 d d d d d c 
            . . . . c b 5 5 b b c c c c c c 
            . . . . c c c c c c . . . . . . 
            . . . . . c b b b c . . . . . . 
            `,img`
            . . . . . . . . . . . . . . . . 
            . . . . c c c c . . . . . . . . 
            . . c c 5 5 5 5 c c . . . . . . 
            . c 5 5 5 5 5 5 5 5 c . . . . . 
            c 5 5 5 5 5 1 f 5 5 5 c . . . . 
            c 5 5 5 5 5 f f 5 5 5 5 c . . . 
            c c b b 1 b 5 5 5 5 5 5 c . . . 
            c c 3 3 b b 5 5 5 5 5 5 d c . . 
            c 5 3 3 3 5 5 5 5 5 d d d c . . 
            . b 5 5 5 5 5 5 5 5 d d d c . . 
            . . c b b c 5 5 b d d d d c . . 
            . c b b c 5 5 b b d d d d c c c 
            . c c c c c c d d d d d d d d c 
            . . . c c c c d 5 5 b d d d c c 
            . . . c b c c b 5 5 b c c c . . 
            . . . c c c d 5 5 b c . . . . . 
            `,img`
            . . . . . . . . . . . . . . . . 
            . . . . c c c c . . . . . . . . 
            . . c c 5 5 5 5 c c . . . . . . 
            . c 5 5 5 5 5 5 5 5 c . . . . . 
            c 5 5 5 5 5 1 f 5 5 5 c . . . . 
            c 5 5 5 5 5 f f 5 5 5 5 c . . . 
            c 5 5 5 5 5 5 5 5 5 5 5 c . . . 
            c c b b 1 b 5 5 5 5 5 5 d c . . 
            c 5 3 3 3 5 5 5 5 5 d d d c . . 
            . b 5 5 5 5 5 5 5 5 d d d c . . 
            . . c b b c 5 5 b d d d d c . . 
            . c b b c 5 5 b b d d d d c c c 
            . c c c c c c d d d d d d d d c 
            . . . c c c c d 5 5 b d d c c . 
            . . c b b c c c 5 5 b c c . . . 
            . . c c c c c d 5 5 c . . . . . 
            `],
        500,
        true
        )
    }
}
function determine_pet_full () {
    playerHand.setPosition(15, 75)
    if (pet_int == 0) {
        animation.runImageAnimation(
        pet_egg,
        [img`
            . . . . . . . . . . . . . . . . 
            . . . b 5 b . . . . . . . . . . 
            . . . . b 5 b . . . . . . . . . 
            . . . . b b b b b b . . . . . . 
            . . . b 5 5 5 5 5 b b . . . . . 
            . . b 5 5 5 5 5 5 5 b b b b b . 
            . . b 5 5 5 5 5 5 5 5 b 5 d b . 
            . . f 4 d 5 f 1 d 5 b 5 5 b . . 
            . . c 4 4 5 f f 1 b 5 5 d b . . 
            b 4 4 4 4 4 b f d 5 5 5 b d b b 
            . b 4 4 4 4 4 5 b 5 5 d c d d b 
            . b 5 5 5 5 5 5 5 b c c d d d c 
            . b 5 5 5 5 5 5 5 d d d d d b c 
            . b d 5 5 5 5 5 d d d d d d c . 
            . . b b 5 5 5 d d d d d b c . . 
            . . . b b c c c c c c c c . . . 
            `,img`
            . . . b 5 b . . . . . . . . . . 
            . . . . b 5 b . . . . . . . . . 
            . . . . . c b . . . . . . . . . 
            . . . . b b b b b b . . . . . . 
            . . . b 5 5 5 5 5 b b . . . . . 
            . . f d 5 5 f 1 d 5 b b . . . . 
            . . c 4 d 5 f f 1 5 5 b . . . . 
            . . 4 4 d d b f d 5 5 b . . . . 
            b 4 4 4 4 4 5 5 5 d b b d d d b 
            . b 4 4 4 4 4 5 5 b 5 5 5 d b b 
            . . b 5 5 5 5 5 d 5 5 5 5 c d b 
            . b 5 5 5 5 5 5 b 5 5 d c d d c 
            . b 5 5 5 5 5 5 5 b c c d d b c 
            . b d 5 5 5 5 5 d d d d d d c . 
            . . b b 5 5 5 d d d d d b c . . 
            . . . b b c c c c c c c c . . . 
            `,img`
            . . . b 5 b . . . . . . . . . . 
            . . . . b 5 b . . . . . . . . . 
            . . . . b b b b b b . . . . . . 
            . . . b 5 5 5 5 5 b b . . . . . 
            . . c 4 d 5 f 1 d 5 b b . . . . 
            b 4 4 4 d d f f 1 5 5 b . . . . 
            . b 4 4 4 4 b f d 5 5 b . . . . 
            . . b 4 4 4 4 5 5 5 5 d b . . . 
            . . b 5 5 5 5 5 5 5 5 d d b . . 
            . b 5 5 5 5 5 5 5 5 d d d d b . 
            . b 5 5 5 5 5 5 5 b b b d d d b 
            . b 5 5 5 5 5 5 c d 5 5 b d d c 
            . b 5 5 5 5 5 5 d c d 5 d b b c 
            . b d 5 5 5 5 5 d d c b 5 5 b . 
            . . b b 5 5 5 d d d d c c c b b 
            . . . b b c c c c c c c c . . . 
            `,img`
            . . . b 5 b . . . . . . . . . . 
            . . . . b 5 b . . . . . . . . . 
            . . . . b b b b b b . . . . . . 
            . . . b 5 5 5 5 5 b b . . . . . 
            . . c 4 d 5 f 1 d 5 b b . . . . 
            b 4 4 4 d d f f 1 5 5 b . . . . 
            . b 4 4 4 4 b f d 5 5 b . . . . 
            . . b 4 4 4 4 5 5 5 5 d b . . . 
            . . b 5 5 5 5 5 5 5 d d d b b . 
            . b 5 5 5 5 5 5 5 b b b d d d b 
            . b 5 5 5 5 5 5 c d 5 5 b d d c 
            . b 5 5 5 5 5 5 d c d 5 d b b c 
            . b 5 5 5 5 5 5 d d c b 5 5 b c 
            . b d 5 5 5 5 5 d d d c c c b b 
            . . b b 5 5 5 d d d c c . . . . 
            . . . b b c c c c c . . . . . . 
            `,img`
            . . . b 5 b . . . . . . . . . . 
            . . . . b 5 b . . . . . . . . . 
            . . . . b b b b b b . . . . . . 
            . . . b 5 5 5 5 5 b b . . . . . 
            . . f d 5 5 f 1 d 5 b b . . . . 
            . . c 4 d 5 f f 1 5 5 b . . . . 
            . . 4 4 d d b f d 5 5 b . . . . 
            b 4 4 4 4 4 5 5 5 5 5 d b b b . 
            . b 4 4 4 4 4 5 5 d b b d d d b 
            . . b 5 5 5 5 5 5 b 5 5 5 d b b 
            . b 5 5 5 5 5 5 d 5 5 5 5 c d c 
            . b 5 5 5 5 5 5 b 5 5 d c d b c 
            . b d 5 5 5 5 5 d b c c d d c . 
            . . b b 5 5 5 d d d d d b c . . 
            . . . b b c c c c c c c c . . . 
            . . . . . . . . . . . . . . . . 
            `],
        500,
        true
        )
    } else if (pet_int == 1) {
        animation.runImageAnimation(
        pet_egg,
        [img`
            . . . . . . c c c c c c . . . . 
            . . . . . c 6 7 7 7 7 6 c . . . 
            . . . . c 7 7 7 7 7 7 7 7 c . . 
            . . . c 6 7 7 7 7 7 7 7 7 6 c . 
            . . . c 7 7 7 c 6 6 6 6 c 7 c . 
            . . . f 7 7 7 6 f 6 6 f 6 7 f . 
            . . . f 7 7 7 7 7 7 7 7 7 7 f . 
            . . c f 6 7 7 c 6 7 7 7 7 f . . 
            . c 7 7 f 6 7 7 c c c c f . . . 
            c 7 7 7 7 f c 6 7 7 7 2 7 c . . 
            c c 6 7 7 6 c f c 7 7 2 7 7 c . 
            . . c 6 6 6 c c f 6 7 1 1 1 1 c 
            . . f 6 6 6 6 c 6 6 1 1 1 1 1 f 
            . . f c 6 6 6 6 6 1 1 1 1 1 6 f 
            . . . f 6 6 6 1 1 1 1 1 1 6 f . 
            . . . . f c c c c c c c c c . . 
            `,img`
            . . . . . . . c c c c c c . . . 
            . . . . . . c 6 7 7 7 7 6 c . . 
            . . . . . c 7 7 7 7 7 7 7 7 c . 
            . . . . c 6 7 7 7 7 7 7 7 7 6 c 
            . . . . c 7 7 7 c 6 6 6 6 c 7 c 
            . . . . f 7 7 7 6 f 6 6 f 6 7 f 
            . . . . f 7 7 7 7 7 7 7 7 7 7 f 
            . . . . f 6 7 7 c 6 7 7 7 7 f . 
            . . c c c f 6 7 7 c c c c f . . 
            . c 7 7 7 c c f 7 7 7 2 6 c . . 
            c 7 7 7 7 6 f c 7 7 2 7 7 6 c . 
            c c c 6 6 6 c 6 6 7 1 1 1 1 c . 
            . . c 6 6 6 6 6 6 1 1 1 1 1 c . 
            . . c 6 6 6 6 6 1 1 1 1 1 6 c . 
            . . c c 6 6 7 1 1 1 1 1 6 c . . 
            . . . c c c c c c c c c c . . . 
            `],
        500,
        true
        )
    } else if (pet_int == 2) {
        animation.runImageAnimation(
        pet_egg,
        [img`
            . . . . . . . . . . . . . . . . 
            . . . . c c c c . . . . . . . . 
            . . c c 5 5 5 5 c c . . . . . . 
            . c 5 5 5 5 5 5 5 5 c . . . . . 
            c 5 5 5 5 5 1 f 5 5 5 c . . . . 
            c 5 5 5 5 5 f f 5 5 5 5 c . . . 
            c 5 5 5 5 5 5 5 5 5 5 5 c . . . 
            c c b b 1 b 5 5 5 5 5 5 d c . . 
            c 5 3 3 3 5 5 5 5 5 d d d c . . 
            . b 5 5 5 5 5 5 5 5 d d d c . . 
            . . c b b c 5 5 b d d d d c c . 
            . c b b c 5 5 b b d d d d c d c 
            . c c c c c c d d d d d d d d c 
            . . . c c c c d 5 5 b d d d c . 
            . . c c c c c b 5 5 b c c c . . 
            . . c b b b c d 5 5 b c . . . . 
            `,img`
            . . . . c c c c c . . . . . . . 
            . . c c 5 5 5 5 5 c . . . . . . 
            . c 5 5 5 5 1 f 5 5 c . . . . . 
            c 5 5 5 5 5 f f 5 5 5 c . . . . 
            c 5 5 5 5 5 5 5 5 5 5 5 c . . . 
            c c b b 1 b 5 5 5 5 5 5 c . . . 
            c 5 3 3 3 5 5 5 5 5 5 5 d c . . 
            c 5 3 3 3 5 5 5 5 5 d d d c . . 
            . c 5 5 5 5 b 5 5 5 d d d c . . 
            . . c b b c 5 5 b d d d d c . . 
            . c b b c 5 5 b b d d d d c c c 
            . c c c c c c d d d d d d d d c 
            . . . . c c c b 5 5 b d d d c . 
            . . . . . c d 5 5 b b c c c . . 
            . . . . c c c c c c c . . . . . 
            . . . . c b b b c . . . . . . . 
            `,img`
            . . . . c c c c c . . . . . . . 
            . . c c 5 5 5 5 5 c . . . . . . 
            . c 5 5 5 5 1 f 5 5 c . . . . . 
            c 5 5 5 5 5 f f 5 5 5 c . . . . 
            c 5 5 5 5 5 5 5 5 5 5 5 c . . . 
            c c b b 1 b 5 5 5 5 5 5 c . . . 
            c 5 3 3 3 5 5 5 5 5 5 5 d c . . 
            c 5 5 5 5 5 5 5 5 5 d d d c . . 
            . c 5 5 5 5 b 5 5 5 d d d c . . 
            . . c b b c 5 5 b d d d d c . . 
            . c b b c 5 5 b b d d d d c c c 
            . c c c c c c d d d d d d d d c 
            . . . . c c b 5 5 b d d d c c . 
            . . . . c d 5 5 b b c c c . . . 
            . . . . c c c c c c c . . . . . 
            . . . . c b b b c . . . . . . . 
            `,img`
            . . . . c c c c c . . . . . . . 
            . . c c 5 5 5 5 5 c . . . . . . 
            . c 5 5 5 5 1 f 5 5 c . . . . . 
            c 5 5 5 5 5 f f 5 5 5 c . . . . 
            c 5 5 5 5 5 5 5 5 5 5 5 c . . . 
            c c b b 1 b 5 5 5 5 5 5 c . . . 
            c 5 3 3 3 5 5 5 5 5 5 5 d c . . 
            c 5 5 5 5 5 5 5 5 5 d d d c . . 
            . c 5 5 5 5 b 5 5 5 d d d c . . 
            . . c b b c 5 5 b d d d d c . . 
            . c b b c 5 5 b b d d d d c c . 
            . c c c c c b b d d d d d d c c 
            . . . c c 5 5 b 5 5 d d d d d c 
            . . . . c b 5 5 b b c c c c c c 
            . . . . c c c c c c . . . . . . 
            . . . . . c b b b c . . . . . . 
            `,img`
            . . . . . . . . . . . . . . . . 
            . . . . c c c c . . . . . . . . 
            . . c c 5 5 5 5 c c . . . . . . 
            . c 5 5 5 5 5 5 5 5 c . . . . . 
            c 5 5 5 5 5 1 f 5 5 5 c . . . . 
            c 5 5 5 5 5 f f 5 5 5 5 c . . . 
            c c b b 1 b 5 5 5 5 5 5 c . . . 
            c c 3 3 b b 5 5 5 5 5 5 d c . . 
            c 5 3 3 3 5 5 5 5 5 d d d c . . 
            . b 5 5 5 5 5 5 5 5 d d d c . . 
            . . c b b c 5 5 b d d d d c . . 
            . c b b c 5 5 b b d d d d c c c 
            . c c c c c c d d d d d d d d c 
            . . . c c c c d 5 5 b d d d c c 
            . . . c b c c b 5 5 b c c c . . 
            . . . c c c d 5 5 b c . . . . . 
            `,img`
            . . . . . . . . . . . . . . . . 
            . . . . c c c c . . . . . . . . 
            . . c c 5 5 5 5 c c . . . . . . 
            . c 5 5 5 5 5 5 5 5 c . . . . . 
            c 5 5 5 5 5 1 f 5 5 5 c . . . . 
            c 5 5 5 5 5 f f 5 5 5 5 c . . . 
            c 5 5 5 5 5 5 5 5 5 5 5 c . . . 
            c c b b 1 b 5 5 5 5 5 5 d c . . 
            c 5 3 3 3 5 5 5 5 5 d d d c . . 
            . b 5 5 5 5 5 5 5 5 d d d c . . 
            . . c b b c 5 5 b d d d d c . . 
            . c b b c 5 5 b b d d d d c c c 
            . c c c c c c d d d d d d d d c 
            . . . c c c c d 5 5 b d d c c . 
            . . c b b c c c 5 5 b c c . . . 
            . . c c c c c d 5 5 c . . . . . 
            `],
        500,
        true
        )
    }
}
let projectile: Sprite = null
let playerHand: Sprite = null
let pet_egg: Sprite = null
let pet_int = 0
scene.setBackgroundImage(assets.image`myImage`)
let petHunger = 10
music.play(music.stringPlayable("C E G C5 - - - - ", 120), music.PlaybackMode.UntilDone)
game.splash("Welcome to", "CINTEC Tamagotchi!")
game.splash("Congrats!", "You got a pet.")
game.splash("Please take", "good care of it.")
let pets_random = [img`
    . . . . . . . . . . b 5 b . . . 
    . . . . . . . . . b 5 b . . . . 
    . . . . . . b b b b b b . . . . 
    . . . . . b b 5 5 5 5 5 b . . . 
    . . . . b b 5 d 1 f 5 d 4 c . . 
    . . . . b 5 5 1 f f d d 4 4 4 b 
    . . . . b 5 5 d f b 4 4 4 4 b . 
    . . . b d 5 5 5 5 4 4 4 4 b . . 
    . . b d d 5 5 5 5 5 5 5 5 b . . 
    . b d d d d 5 5 5 5 5 5 5 5 b . 
    b d d d b b b 5 5 5 5 5 5 5 b . 
    c d d b 5 5 d c 5 5 5 5 5 5 b . 
    c b b d 5 d c d 5 5 5 5 5 5 b . 
    . b 5 5 b c d d 5 5 5 5 5 d b . 
    b b c c c d d d d 5 5 5 b b . . 
    . . . c c c c c c c c b b . . . 
    `, img`
    . . . c c c c c c . . . . . . . 
    . . c 6 7 7 7 7 6 c . . . . . . 
    . c 7 7 7 7 7 7 7 7 c . . . . . 
    c 6 7 7 7 7 7 7 7 7 6 c . . . . 
    c 7 c 6 6 6 6 c 7 7 7 c . . . . 
    f 7 6 f 6 6 f 6 7 7 7 f . . . . 
    f 7 7 7 7 7 7 7 7 7 7 f . . . . 
    . f 7 7 7 7 6 c 7 7 6 f . . . . 
    . . f c c c c 7 7 6 f c c c . . 
    . . c 6 2 7 7 7 f c c 7 7 7 c . 
    . c 6 7 7 2 7 7 c f 6 7 7 7 7 c 
    . c 1 1 1 1 7 6 6 c 6 6 6 c c c 
    . c 1 1 1 1 1 6 6 6 6 6 6 c . . 
    . c 6 1 1 1 1 1 6 6 6 6 6 c . . 
    . . c 6 1 1 1 1 1 7 6 6 c c . . 
    . . . c c c c c c c c c c . . . 
    `, img`
    . . . . . . . . . . . . . . . . 
    . . . . c c c c . . . . . . . . 
    . . c c 5 5 5 5 c c . . . . . . 
    . c 5 5 5 5 5 5 5 5 c . . . . . 
    c 5 5 5 5 5 1 f 5 5 5 c . . . . 
    c 5 5 5 5 5 f f 5 5 5 5 c . . . 
    c 5 5 5 5 5 5 5 5 5 5 5 c . . . 
    c c b b 1 b 5 5 5 5 5 5 d c . . 
    c 5 3 3 3 5 5 5 5 5 d d d c . . 
    . b 5 5 5 5 5 5 5 5 d d d c . . 
    . . c b b c 5 5 b d d d d c c . 
    . c b b c 5 5 b b d d d d c d c 
    . c c c c c c d d d d d d d d c 
    . . . c c c c d 5 5 b d d d c . 
    . . c c c c c b 5 5 b c c c . . 
    . . c b b b c d 5 5 b c . . . . 
    `]
pet_int = randint(0, 2)
pet_egg = sprites.create(pets_random[pet_int], SpriteKind.Player)
pet_egg.setPosition(80, 75)
let hungerbar = statusbars.create(20, 4, StatusBarKind.Health)
hungerbar.attachToSprite(pet_egg, 5, 0)
hungerbar.setColor(7, 2)
hungerbar.setLabel("Hunger", 4)
forever(function () {
    determine_pet_idle()
    controller.moveSprite(pet_egg, 100, 100)
    pause(10000)
    statusbars.getStatusBarAttachedTo(StatusBarKind.Health, pet_egg).value += -10
})

def determine_pet_happy():
    global projectile
    playerHand.set_position(15, 75)
    if pet_int == 0:
        animation.run_image_animation(pet_egg,
            [img("""
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
                    """),
                img("""
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
                    """),
                img("""
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
                    """),
                img("""
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
                    """),
                img("""
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
                    """)],
            500,
            True)
        projectile = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . .
                . . . . . . 4 4 4 4 . . . . . .
                . . . . 4 4 4 5 5 4 4 4 . . . .
                . . . 3 3 3 3 4 4 4 4 4 4 . . .
                . . 4 3 3 3 3 2 2 2 1 1 4 4 . .
                . . 3 3 3 3 3 2 2 2 1 1 5 4 . .
                . 4 3 3 3 3 2 2 2 2 2 5 5 4 4 .
                . 4 3 3 3 2 2 2 4 4 4 4 5 4 4 .
                . 4 4 3 3 2 2 4 4 4 4 4 4 4 4 .
                . 4 2 3 3 2 2 4 4 4 4 4 4 4 4 .
                . . 4 2 3 3 2 4 4 4 4 4 2 4 . .
                . . 4 2 2 3 2 2 4 4 4 2 4 4 . .
                . . . 4 2 2 2 2 2 2 2 2 4 . . .
                . . . . 4 4 2 2 2 2 4 4 . . . .
                . . . . . . 4 4 4 4 . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            playerHand,
            50,
            0)
    elif pet_int == 1:
        animation.run_image_animation(pet_egg,
            [img("""
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
                    """),
                img("""
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
                    """)],
            500,
            True)
        projectile = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . .
                . . . . . . 4 4 4 4 . . . . . .
                . . . . 4 4 4 5 5 4 4 4 . . . .
                . . . 3 3 3 3 4 4 4 4 4 4 . . .
                . . 4 3 3 3 3 2 2 2 1 1 4 4 . .
                . . 3 3 3 3 3 2 2 2 1 1 5 4 . .
                . 4 3 3 3 3 2 2 2 2 2 5 5 4 4 .
                . 4 3 3 3 2 2 2 4 4 4 4 5 4 4 .
                . 4 4 3 3 2 2 4 4 4 4 4 4 4 4 .
                . 4 2 3 3 2 2 4 4 4 4 4 4 4 4 .
                . . 4 2 3 3 2 4 4 4 4 4 2 4 . .
                . . 4 2 2 3 2 2 4 4 4 2 4 4 . .
                . . . 4 2 2 2 2 2 2 2 2 4 . . .
                . . . . 4 4 2 2 2 2 4 4 . . . .
                . . . . . . 4 4 4 4 . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            playerHand,
            50,
            0)
    elif pet_int == 2:
        animation.run_image_animation(pet_egg,
            [img("""
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
                    """),
                img("""
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
                    """),
                img("""
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
                    """),
                img("""
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
                    """),
                img("""
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
                    """),
                img("""
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
                    """)],
            500,
            True)
        projectile = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . .
                . . . . . . 4 4 4 4 . . . . . .
                . . . . 4 4 4 5 5 4 4 4 . . . .
                . . . 3 3 3 3 4 4 4 4 4 4 . . .
                . . 4 3 3 3 3 2 2 2 1 1 4 4 . .
                . . 3 3 3 3 3 2 2 2 1 1 5 4 . .
                . 4 3 3 3 3 2 2 2 2 2 5 5 4 4 .
                . 4 3 3 3 2 2 2 4 4 4 4 5 4 4 .
                . 4 4 3 3 2 2 4 4 4 4 4 4 4 4 .
                . 4 2 3 3 2 2 4 4 4 4 4 4 4 4 .
                . . 4 2 3 3 2 4 4 4 4 4 2 4 . .
                . . 4 2 2 3 2 2 4 4 4 2 4 4 . .
                . . . 4 2 2 2 2 2 2 2 2 4 . . .
                . . . . 4 4 2 2 2 2 4 4 . . . .
                . . . . . . 4 4 4 4 . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            playerHand,
            50,
            0)

def on_b_pressed():
    global playerHand
    playerHand = sprites.create(img("""
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
            """),
        SpriteKind.enemy)
    animation.stop_animation(animation.AnimationTypes.ALL, pet_egg)
    hungerbar.value += 5
    determine_pet_full()
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_a_pressed():
    global playerHand
    playerHand = sprites.create(img("""
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
            """),
        SpriteKind.enemy)
    animation.stop_animation(animation.AnimationTypes.ALL, pet_egg)
    happybar.value += 5
    determine_pet_happy()
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_zero(status):
    determine_pet_call()
    pause(1000)
statusbars.on_zero(StatusBarKind.health, on_on_zero)

def determine_pet_call():
    if pet_int == 0:
        animation.run_image_animation(pet_egg,
            [img("""
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
                    """),
                img("""
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
                    """),
                img("""
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
                    """)],
            500,
            True)
        animation.run_movement_animation(pet_egg,
            animation.animation_presets(animation.shake),
            2000,
            False)
        animation.run_movement_animation(pet_egg,
            animation.animation_presets(animation.fly_to_center),
            2000,
            False)
    elif pet_int == 1:
        animation.run_image_animation(pet_egg,
            [img("""
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
                    """),
                img("""
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
                    """),
                img("""
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
                    """),
                img("""
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
                    """),
                img("""
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
                    """),
                img("""
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
                    """)],
            500,
            True)
        animation.run_movement_animation(pet_egg,
            animation.animation_presets(animation.shake),
            2000,
            False)
        animation.run_movement_animation(pet_egg,
            animation.animation_presets(animation.fly_to_center),
            2000,
            False)
    elif pet_int == 2:
        animation.run_image_animation(pet_egg,
            [img("""
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
                    """),
                img("""
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
                    """),
                img("""
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
                    """),
                img("""
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
                    """),
                img("""
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
                    """),
                img("""
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
                    """)],
            500,
            True)
        animation.run_movement_animation(pet_egg,
            animation.animation_presets(animation.shake),
            2000,
            False)
        animation.run_movement_animation(pet_egg,
            animation.animation_presets(animation.fly_to_center),
            2000,
            False)
def determine_pet_idle():
    if pet_int == 0:
        animation.run_image_animation(pet_egg,
            [img("""
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
                    """),
                img("""
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
                    """),
                img("""
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
                    """),
                img("""
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
                    """),
                img("""
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
                    """)],
            500,
            True)
    elif pet_int == 1:
        animation.run_image_animation(pet_egg,
            [img("""
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
                    """),
                img("""
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
                    """)],
            500,
            True)
    elif pet_int == 2:
        animation.run_image_animation(pet_egg,
            [img("""
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
                    """),
                img("""
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
                    """),
                img("""
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
                    """),
                img("""
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
                    """),
                img("""
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
                    """),
                img("""
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
                    """)],
            500,
            True)
def determine_pet_full():
    global projectile
    playerHand.set_position(15, 75)
    if pet_int == 0:
        animation.run_image_animation(pet_egg,
            [img("""
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
                    """),
                img("""
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
                    """),
                img("""
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
                    """),
                img("""
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
                    """),
                img("""
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
                    """)],
            500,
            True)
        projectile = sprites.create_projectile_from_sprite(img("""
                ..........bbbbbb................
                .......bbb444444bb..............
                .....2244444ddd444b.............
                ....244444444dddd44e............
                ...244444444444ddd4be...........
                ..244444444444444d44be..........
                .2b444444444444444d4be..........
                .2b44444444444444444bbe.........
                2bbb4444444444444444bbe.........
                2bbb4444444444444444bbe.........
                2bb4b4444444444444444bbe........
                2bb4444444444444444444be........
                2bb44444444444444444444e........
                2bbb444bbb4444444444444e........
                22bbb444bb4bb444444444be........
                .2bbbbb44bbbb44444444bbe........
                .22bbbbbbbb44bbb444444bbe.......
                ..eeebbbbbbb44bbb444444be.......
                ...eeeeebbbbbbbb44b4444be.......
                .....eeeeee222bb44bbb4bbe.......
                .......eeeee222bb44bbbbee.......
                ............e222bbbbbbbec.......
                ..............ee2bbbbeebdb......
                .................eeeeecdddb.....
                .......................cd11bbbb.
                ........................cd111dbb
                .........................b11111c
                .........................c11dd1c
                .........................cd1dbc.
                .........................cb11c..
                ..........................ccc...
                ................................
                """),
            playerHand,
            50,
            0)
    elif pet_int == 1:
        animation.run_image_animation(pet_egg,
            [img("""
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
                    """),
                img("""
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
                    """)],
            500,
            True)
        projectile = sprites.create_projectile_from_sprite(img("""
                ..........bbbbbb................
                .......bbb444444bb..............
                .....2244444ddd444b.............
                ....244444444dddd44e............
                ...244444444444ddd4be...........
                ..244444444444444d44be..........
                .2b444444444444444d4be..........
                .2b44444444444444444bbe.........
                2bbb4444444444444444bbe.........
                2bbb4444444444444444bbe.........
                2bb4b4444444444444444bbe........
                2bb4444444444444444444be........
                2bb44444444444444444444e........
                2bbb444bbb4444444444444e........
                22bbb444bb4bb444444444be........
                .2bbbbb44bbbb44444444bbe........
                .22bbbbbbbb44bbb444444bbe.......
                ..eeebbbbbbb44bbb444444be.......
                ...eeeeebbbbbbbb44b4444be.......
                .....eeeeee222bb44bbb4bbe.......
                .......eeeee222bb44bbbbee.......
                ............e222bbbbbbbec.......
                ..............ee2bbbbeebdb......
                .................eeeeecdddb.....
                .......................cd11bbbb.
                ........................cd111dbb
                .........................b11111c
                .........................c11dd1c
                .........................cd1dbc.
                .........................cb11c..
                ..........................ccc...
                ................................
                """),
            playerHand,
            50,
            0)
    elif pet_int == 2:
        animation.run_image_animation(pet_egg,
            [img("""
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
                    """),
                img("""
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
                    """),
                img("""
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
                    """),
                img("""
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
                    """),
                img("""
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
                    """),
                img("""
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
                    """)],
            500,
            True)
        projectile = sprites.create_projectile_from_sprite(img("""
                ..........bbbbbb................
                .......bbb444444bb..............
                .....2244444ddd444b.............
                ....244444444dddd44e............
                ...244444444444ddd4be...........
                ..244444444444444d44be..........
                .2b444444444444444d4be..........
                .2b44444444444444444bbe.........
                2bbb4444444444444444bbe.........
                2bbb4444444444444444bbe.........
                2bb4b4444444444444444bbe........
                2bb4444444444444444444be........
                2bb44444444444444444444e........
                2bbb444bbb4444444444444e........
                22bbb444bb4bb444444444be........
                .2bbbbb44bbbb44444444bbe........
                .22bbbbbbbb44bbb444444bbe.......
                ..eeebbbbbbb44bbb444444be.......
                ...eeeeebbbbbbbb44b4444be.......
                .....eeeeee222bb44bbb4bbe.......
                .......eeeee222bb44bbbbee.......
                ............e222bbbbbbbec.......
                ..............ee2bbbbeebdb......
                .................eeeeecdddb.....
                .......................cd11bbbb.
                ........................cd111dbb
                .........................b11111c
                .........................c11dd1c
                .........................cd1dbc.
                .........................cb11c..
                ..........................ccc...
                ................................
                """),
            playerHand,
            50,
            0)
projectile: Sprite = None
playerHand: Sprite = None
pet_egg: Sprite = None
pet_int = 0
hungerbar: StatusBarSprite = None
happybar: StatusBarSprite = None
scene.set_background_image(assets.image("""
    myImage
    """))
petHappy = 20
petHunger = 10
music.play(music.string_playable("C E G C5 - - - - ", 120),
    music.PlaybackMode.UNTIL_DONE)
game.splash("Welcome to", "CINTEC Tamagotchi!")
game.splash("Congrats!", "You got a pet.")
game.splash("Please take", "good care of it.")
pets_random = [img("""
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
        """),
    img("""
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
        """),
    img("""
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
        """)]
pet_int = randint(0, 2)
pet_egg = sprites.create(pets_random[pet_int], SpriteKind.player)
pet_egg.set_position(80, 75)

def on_forever():
    global happybar, hungerbar
    happybar = statusbars.create(20, 4, StatusBarKind.health)
    hungerbar = statusbars.create(20, 4, StatusBarKind.health)
    happybar.attach_to_sprite(pet_egg)
    hungerbar.attach_to_sprite(pet_egg, 5, 0)
    hungerbar.set_color(7, 2)
    happybar.set_color(7, 2)
    hungerbar.set_label("Hunger", 4)
    happybar.set_label("Happy", 4)
    for index in range(1):
        determine_pet_idle()
        controller.move_sprite(pet_egg, 100, 100)
        pause(1000)
    happybar.value -= 1
    hungerbar.value -= 1
forever(on_forever)

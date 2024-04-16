import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")

    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img,True,False)
    kk_img = pg.transform.rotozoom(kk_img,10,1.0)
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        fonto = pg.font.Font(None,80)
        txt = fonto.render("hello",True,(255,255,255))

        screen = pg.display.set_mode((800,600))
        img = pg.image.load("fig/3.png")
        enn = pg.Surface((20,20))
        pg.draw.circle(enn,(255,0,0),(10,10),10)
        txt = fonto.render("hello",True,(255,255,255))
        screen.blit(img,[300,200])
        pg.display.update()

        img_rct = img.get_rect()
        img_rct.center = 300,200
        screen.blit(img, img_rct)
        screen.blit(bg_img, [0, 0])
        pg.display.update()
        tmr += 1        
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
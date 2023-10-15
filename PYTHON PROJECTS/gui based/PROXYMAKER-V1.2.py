import flet
import csv 


def main(page: flet.page):
    page.bgcolor = "#F2F3F4"
    page.title = "Proxy Maker v 2.0 by sameer"
    page.scroll = "adaptive"
    
    # page.controls.append()
    page.update()
    
if __name__ == '__main__':
    flet.app(target=main)
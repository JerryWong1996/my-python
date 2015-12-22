# -*- coding: utf-8 -*-

import Image, ImageDraw, ImageFont

original_pic = "target.jpg"
saved_pic = "goal.jpg"
windows_font = "msyh.ttf"
color = (255, 0, 0)

def draw_text(text, fill_color, windows_font):
	
	im = Image.open(original_pic)
	font = ImageFont.truetype(windows_font, 35)
	x, y = im.size
	draw = ImageDraw.Draw(im)
	draw.text((x-20, 7), text, fill_color,font = font)
	im.save(saved_pic)
	im.show()


if __name__ == "__main__":
	
	number = str(raw_input('Please enter the number: '))
	draw_text(number, color, windows_font)
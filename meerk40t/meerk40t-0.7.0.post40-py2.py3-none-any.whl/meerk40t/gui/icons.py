# ----------------------------------------------------------------------
from wx import Bitmap
from wx.lib.embeddedimage import PyEmbeddedImage as PEI

DARKMODE = False
icon_r = 230
icon_g = 230
icon_b = 230


class PyEmbeddedImage(PEI):
    def __init__(self, data):
        super().__init__(data)

    def GetBitmap(self, use_theme=True, resize=None):
        image = PEI.GetImage(self)
        if DARKMODE and use_theme:
            image.Replace(0, 0, 0, icon_r, icon_g, icon_b)
        if resize is not None:
            image = image.Scale(*resize)
        return Bitmap(image)


icons8_add_file_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAAAXNSR0IArs4c6QAAAARnQU1B"
    b"AACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAALdSURBVGhD7Zq5qhRBFIYH10BETFxQ"
    b"UUEMBCMFF0xMFBNBcF8QDBTEB/ANTAVxx9DtGcw0ckP0BUTcMFFQEVxQ/w/mwKHt7ntmqqrn"
    b"Cv3DF3RNVU39XVOnTtW9g169emXRJrEvM+tE57op/mTmi9gmOlUJI9C5GW/kvXiSwHcxMTPe"
    b"yDkKEvRKeCPQmZnSRqATM6WMnBc/3HNxM6WMMOi9ojMzJY2gzsyUNoI6MVPKyGfx0fFT2GeA"
    b"GbKKbCplJALfnU29kRqtFxum4IKY9kYiOit6I23qjYyp3shU6o2Mqf/SyFyxS1wVnCDfiV/C"
    b"vu+F2C5miGSVMDJLnBQM3Ppu46U4LpIM5TayQjwVfqBR7otlYizlNLJRcIHhB0eWe0scFlvE"
    b"GrFVHBG3xVfh69OeVGdk5TKyXHwQ1tdvcUksEm1aIi4L6lvb12K1GEk5jLAmngnr55vYL0bR"
    b"AUE76+OBGGnN5DBySlgfvFkGVdU8cc/Bc1UHhZ+ZMyKsVCOEWB+dLoo6LRBWB3iu0xVhdTjf"
    b"MNshpRphn7D2LOymNRE1slj4ALBbhJRqhM3O2hOdmhQ1gu4Iq9c0w/8o1Qg7trUnpJrmi4WO"
    b"lcLqAc/+c+qbjgmrRxAJKdWI3zc2UzAUUcfKI1DfxH5j5YT0kFKN+Bv4tRQMlWKEfqyc+7CQ"
    b"puOMsPNb+VsKIsq5Ro5SMFSuNfKYgohSjZCGWHtypyaNErXuCqtH/yGlGtkhrD3xn32gTlEj"
    b"S4XfR+g/JG9knD+9PRfWHpreYNTIdWF1SB7niJC8kRyQK5EzVRXJtQ4Jn2udEGHlNgJksXWJ"
    b"Y5sw4bPfh2KmCCvXPwywq/NTsIHwZjln8JtvE59fE34mSEI530xMnP68GWDhEoUIzewPdkIk"
    b"xFJePSFigsvuiWuVeCT84KLQbqIzURVniNOien5v4o1gYWe5Fiqh2WKPuCHIYj8J7rVIO3j7"
    b"hOqdoiXEDgZ/AYB+bilw1gi8AAAAAElFTkSuQmCC"
)

# ----------------------------------------------------------------------
icons8_comments_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAAAXNSR0IArs4c6QAAAARnQU1B"
    b"AACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAEcSURBVGhD7Zm7DcIwFEWzBzOwARvQ"
    b"0LAKtJSUtIxAzwAMQEXJAkhUbADvFpaiyI7jzzN2dI90msRx3pH4REpHCCGEEDtL8Vy5mNHL"
    b"WvxWLmb0MsuQt3isRMwSHfLAgUrALAxhiAJqITfxnlns6UIt5COadbnEni4YAsdCNuI2s9jT"
    b"hVpIaRjiCzmItkeJFLGnC7UQ/mqN+JeQ2Xy0SsMQX0jKH+JKDEUtJOXLfhVDYQgcC0l5jD+J"
    b"oaiFlIYhDFEiKeQl7iNciC5wznaNT8wSHRLrU7TF4BjO2a4JsVgIHMbkioCTQlJeK1zE/g1N"
    b"jC0Ca217THHSa4VUdmJ/YAQMI7CmCYYxfZuJMNhimosw9GOajTAgoPkIQtqm634PwFqxOUO9"
    b"7wAAAABJRU5ErkJggg=="
)

# ----------------------------------------------------------------------
icons8_connected_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAAAXNSR0IArs4c6QAAAARnQU1B"
    b"AACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAKaSURBVGhD7ZjLrkxBFIabEIIEcyaI"
    b"4BnELSRuMWQk4QGEiaEQnsCEEQ+AgYmIRI7BSZi4DzwGIi4Dcfk+rGRlp7vP3rprdw/qS744"
    b"e+tOrb+7q2rtGlQqlUqlUplfVuEd3P3nao44iDdxEV/jY7yGO7GJIR7iL/yEcxFmOz5Dixrm"
    b"D7yN61ByiPAuzpR9+B5zUaN8g5uwGcLr1dgrK3H93z8Hh/ELRkE/8T6exRN4AV9iLvpr43pm"
    b"IfwJvMBT+A2jIAMdxSbL8Arm4sOZhhhWkCH8iY3jIub3+M1sxl4xxHK8hbmYKOgQtqEZ5i2u"
    b"xV6Ib8IQw8K8w43YlmYYV7PiNH9Oo8I4Z7qEyXPGpXkHFsXVySJz0YZY8e/ffL9LGBeA5xjv"
    b"vYTFcXXKBes0wrg0x/tcvYriPpGX2OykYY5jvMe9phgup3mzc3VyYse1ThLmDMbr7cmKsA0/"
    b"YgxkIJdYi5vWnLEDiNde90YJnmIM8hnzZjeNMHYAtjPxuv04dfzkYwAHO4JNJgnjh+KHE/+/"
    b"iEW4gTHIPW+M4H/C+LyS590H9GdchCcYA532xhi6hHGhyJ2vgfZgMV5hDHbMG0vQJUxoiANY"
    b"lEcYA573Rgu6hjmJxbmKMaBthO1EG7rOmQ1YlF1oIxeD2uC1pW0YG1HvFcfWOhdj690Ww4zr"
    b"AHoLIWvQh55cTNsw7kPN53KNML2FCLbid8zFLBVmL+Z9ItvrNxEMO3cKL+OwBcClOu/YBvIR"
    b"wDkzNyGa34zFnUN7Jo9+bABz75T3CVenuQjh9Rb0cC3fH6WHdUV37DZ4oJyLMkScO3nc6YTN"
    b"S3NTG8BivVMXPEj2QNmicoiMBwU+Yz9AN8wF9HmiSCs+CYZxcvZ+AlipVCqVSqUVg8FvvyiE"
    b"Su2rldYAAAAASUVORK5CYII="
)

# ----------------------------------------------------------------------
icons8_down = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAAAXNSR0IArs4c6QAAAARnQU1B"
    b"AACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAD7SURBVGhD7Y9JCgIxFAV77bTUe7h2"
    b"PIIX0a2H8SyC0xH0IA4LN+r7yoMgjbZ00ibwCgqSQH5SmRBCCCGEEEKI6pjA6WsZnDpcwM5z"
    b"5xGLuMIbnNlBQCxiBe/wAL3FMMIGmyFj3Ai6h21YmjG8QHd4iBiLWEP3HXMJa9ALIxgypgGD"
    b"R5AhDBFTaQTxHWMRG+jOM4NGEF8xTfi3CDKAZWKiiCAWc4buR4rEWMQWuvfMv0SQX2OijCB9"
    b"WCSmBaONIN9ikoggFnOC7kctZg53zhmNMoLkxeQZdQTpwU8xSUQQiznCpCPIe0ySEYQxSUeQ"
    b"Lkw+QgghhBBCJE+WPQBgjKllZBue5gAAAABJRU5ErkJggg=="
)

# ----------------------------------------------------------------------
icons8_left = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAAAXNSR0IArs4c6QAAAARnQU1B"
    b"AACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAADASURBVGhD7c+5DcJAAERRx1wh9EHM"
    b"WQKNQEox1ILEVQIUwhGQAH9lnKy0sXfs+dKTJp3COeecE2yJVTl1W+CFN2TPzBFOfP8kz8Qn"
    b"gg/WkCl1YgOZZvCJHAonnpA+MYVP5FBjTjwgfWICn8ihcOIOn6i7MeITwRZSdbBHfOSCAaRK"
    b"nTmjUWf6kMpnci115oRGnelBqlacOaJRZ7qQqhVnDvCZOkud2UGu+MwNI0hWnblC9kRVODMs"
    b"p3POOVd3RfEDYnipZR7hKKAAAAAASUVORK5CYII="
)

# ----------------------------------------------------------------------
icons8_right = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAAAXNSR0IArs4c6QAAAARnQU1B"
    b"AACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAADYSURBVGhD7ZHJCQJREAUHvbkdNQUD"
    b"8OgagoloQmbhXXALQQNxOYigVjszoDBzUobpzysofv++FR0JIYQQP1BN3n/Rxife3z+ndPCA"
    b"K6zZwiMWcUS7huk2ZoFphOuYOq5RMWXDYjaomLLRwKBitqiYstHEoGJ2qJiyEVRMC4OK2ePf"
    b"YirJWzQnXMbjFz3sxqMP5vjAz2tYXB/dEGzEGRVRNHkRA3RDVsQFFVE0QUcM0Q1ZEVdURNHk"
    b"RYzQDTN0H2FM8YauI1LSGIsY28IzFjOJRyGEEMILUfQCpm2nw/NYYCkAAAAASUVORK5CYII="
)

# ----------------------------------------------------------------------
icons8_home_filled_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAAAXNSR0IArs4c6QAAAARnQU1B"
    b"AACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAHeSURBVGhD7dk9SxxRGMXxJUGSqBhE"
    b"LGwUVLSxkFjEIvoFtDGVtVYRxNQpAkkVrCwTsUlAzDdIpY2lghAiaGMQBUsJgSiKJv8DzjLM"
    b"Pjp3ZncmV7gHfrhv83KQee6wWwlxyxh2sYo2vXAfs4AL/L2xjyHcm7RiDVGBuN+YhvcZwA9Y"
    b"JeKW0IR49Lzd0IJSM4VfsE7csokuRJmA9TldX6XkIT7gGtaJ3OUEGgjKY6wg+ZlSinRiHcmD"
    b"Z3GJ14gyizNE7xde5DmOED+penyFBoUygp/Q64UWeYVzJE+mXlpzBqF04BsKKfIEn2GdRKNo"
    b"YLyE8gDRNdSw9GIH1sEbTYNjERokDY1G4ymsgxZpAxoodUf/2ne4gnWgMhxjFLkTXWzWzsum"
    b"wTKHzHmGA1g7/Z++oBlOmUF8QfKNBk4fbs0jLMPa2DcaPJOoSTe2YG3kK43o99BAquYQejP6"
    b"6ztNMt2j6fEbVKO7Tq3YPUhu5CPdtoxD64zWuJo8hbWhb1Lvv0KRkoUivglFfFNokT/YzmAP"
    b"1n5cFFrkO7LkBaz9uAhFXIQiOYQiLkKRHEIRF6FIDqGIi1Akh1DERSiSQ2oRfdOd52dmKbOI"
    b"vkxMzTw+5fAWWdIPaz9pPmIYISHFp1L5B9V7aqEmmt6rAAAAAElFTkSuQmCC"
)

# ----------------------------------------------------------------------
icons8_disconnected_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAAAXNSR0IArs4c6QAAAARnQU1B"
    b"AACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAMOSURBVGhD7ZlNqw9RHMf/QhQKb4Cw"
    b"s7pRVh4SEeXhFXhcWJPssLAkL4CFlLhuNxJRHha8EHZuoTxbie+HfvXrdGb+Z2ZOM2cx3/rU"
    b"nfnPw+9zZ+acM2cmY8aMGVNSlosbYv2/pYKyTVwR8+KZuCVOi7UiDBJPxR/xVhQhs1G8EBQV"
    b"44u4IBYJ4iUMrsyg2S4+CV9UFQ/EKhFKsIxcr1kiFv//c7Jf/BC+qJfivDgjrosF4X//ECwP"
    b"JjEn7ouD4pewghA6LMJwBdjeF28MKhErCIldoipcwdvC78PtiGTvWSHeCF8MILFXTEtM5qGw"
    b"BqDXrBShzCvB1UpJTIbWbJDEZHgGmsjMCtv3s1gjBgkyr0VbGfZ/L2zfY2KwbBa/RVuZa8L2"
    b"G6wzXCcYVngJI1XmpLB9HrGi7zAmCiXeBcspMueEbX+PFX0mJnFRtHlmGAHYtpdZkSOckH6i"
    b"LqtFTMLSROao8NttEZ3DieixaVIppi785+zkXsKSIrNPfBf2O8OUzjEJO2iqTEzCwv5VzwwS"
    b"fnzGAHKD6Bw6J07iT5oiU5dLwh/PYAQQDjJ3iGw5IPwJoa1MKBH2MwYSu0W2cDAOGjtZU5lQ"
    b"goaBTjN8ZoB/XrZwWb3ET8Hl9ydMlYlJ0GkS9uc4/neey1hr1jibxEdhB0Zoj+DgbZ4Z35oh"
    b"EU4khDLZRJ4LOyhNoX8p6iITk7CYTDaJrcIXeUSEaStDp1kXOt0sEsTfBkzhVKWtTG/xHeBZ"
    b"VtSkaJnHwoo6wYopKVbmprCCrrIiIUXK8FppxTB5Nm3UaylOhgll5mKtGJ4ZxlwpKU6GKRhf"
    b"zB3RRKbtCCB7mBRjQtkXw+smRU4LI4DY+AyZ1Ns0a5hL+iZ8MdxmS0VVdoqqQWa2HrtJlolw"
    b"at8XFLtNDgn/ZocQo1i2L0bia7DM5BlN8ynBbEf4TCBh7xMI9C4R+1LEMi1Z+MxUwaiZjzuD"
    b"hhk9XxQS9n2CBoDWjLlYv42H74JZ3rG7xs9LeQkfrs5xgfQTcVcw0JwRRQUZiuz9S9GYMWPG"
    b"VGQy+Qs7CKtFP8P3cgAAAABJRU5ErkJggg=="
)

# ----------------------------------------------------------------------
icons8_gas_industry_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAAAXNSR0IArs4c6QAAAARnQU1B"
    b"AACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAVlSURBVGhD7Zl3yIVTHMdfe0cie0XI"
    b"yN6SkWQkW0b+IFvJLpFNQsmKJCs7QoSUnZA9IitbSPaen8+5z6/3eU/n3vd93ee5977lW5/u"
    b"8zu/Z5zzPGf8fueODVCLwDXwHWxpwUzTHHAcfAP/VBwAM0qrwfMQDfi1+t0YZoRmgWPhF7Di"
    b"H8EecFNlrwkjr/nhLoivcB0sCOpqsGzzZI2wloWXwMo6JnaHuk4EfUcma0Rlv/8crOgbsDLk"
    b"2hT0P5CsEdRW8CNYyXtgAShpNvgM/oBSQ4eqreEnsBEOZivbS+eA596QrBGRs8+3YMVc7CZr"
    b"hHJh/B78KqtaMGwtBR9DvF2n3JJcEHOdBV73GHS7biCyck+BlXka5oSS9gNDkiuTNS6n40/A"
    b"6w+1YFg6H6yEX2QxCzL5li8AzxEngFw7gz675tIWDFrrwp/wG6xnQSYbcRVEI+RcKOk20P8g"
    b"DLSLOZgjdjrDgoLOA/2/g93O432hpEXhC/CcgywYlOzzPvRtKI2LvUC/X2xPcGxo94qtjME8"
    b"x5nMCaR1zQpvgg/d24JMy0GE6kdYgBwb2oYuvXQneJ5xWevaFXyY4UepP98L+m9JVkdPgmUR"
    b"NHaTDf0Z/oaNLGhTEdEenqyJ2gT0fQ32+1A0ZN5kdeSCOHvncILOBM91XLWmhcCkSEpx1MNg"
    b"JU5K1riiIUsmqxNY+uavTdZE2VjjMM9vLRV24PqAh5I1USuCXcLBai5SV3zF9cGv8FZlvwcl"
    b"nQL6692zUV0EPsCsL5dfQV9poF4G+g6GXapjMc6qd7eQYyVeytwWNK0nwAoY6ebyK+lzGs3l"
    b"JoM+Fz7jsWiIbAslPQv6S8/qW5+CNy+FI5FMlcIMx4ZvX3zLvu3rwfMvh5IuBv3HJ6thxSZC"
    b"Pu3OB5br76YIQ+QdWKE6/gpKi6pBpP4rktWg5gFvbHCXawnQ52zTTatAbAM5+NVzoG3gmMs8"
    b"X58voFE56LzxD8maqGiI2z29ZGhj7HVgsjobdl5nRpkrGlLy9S3nfm+ezyR2Dcvt/5OpnmAt"
    b"A44XX04+ex0G3tOx0rgi4nUXJJeN0DdXsqauWCzz7uUkYPkxyWpYMZOYouaKQNJFbzo6Hbzu"
    b"7GSNKxbNDZLVsDYEb256mnevmE4PSdbUFdHCrcnqyKTNMme0UjzWiCJHPzlZ47IBlt+RrKnL"
    b"BdHr7k9WR7FoGkm0JgO+SHHroXbEWg7c6YwTcxorHdPs2uD9nd1WsqBNxebal7C6BZUeB8ud"
    b"ZqeqS8BrTgXXqpcru5XZKpc5e2R9bvNsD2p/sOyZZE0up+3I1deBm6vj98GUYSCyEvH3gF3h"
    b"QvDh71ZlO8Fk2gc89xWI/0zcdl0LBq4TwGDQSvh2I2p9HXptnbowxpQd17sWbQNDk7sjsbDV"
    b"ORq6yRdQP9fu1MqaMV0ZEbsxEV9EHD/uuuSyTJ/nOPs54POsciTkguaYcSbqJtchN/cij/9f"
    b"/0UueruBYYUsD8r4KsqC2C10i6hebiocGeYWUPcZurtNpBz0Ub4dmLw1IkMQp9no//IaLAx5"
    b"uRjKuOvoap/7DEfWyMoC15LNsjL5APreSnVwug36F7iteR948w/BHQ+Pnf9vh9iEeBWczTw2"
    b"q9T3SGU7w/nXtMcGhnWf996xOjbj1Bfpg+OuL7nV6Y0izY3KWwl3HD22USoqrx0ZoI1SUXnX"
    b"DycCj22UCt8LEDv5NkpFw/rOFvOGLA7addxQUObmue9FUJEG1HkUVKk73Q2qtYYoN+T8Iydw"
    b"ElCuJ6dB3bcDKHMLE6i6z7+0lRGz/4DVfU4UqvGGmLM76AfNpdBIQ1x1vdGwuRH61lFQ/+yD"
    b"xo06k64eGhv7Fz7x+0gwmZssAAAAAElFTkSuQmCC"
)

# ----------------------------------------------------------------------
icons8_laser_beam_52 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADQAAAA0CAYAAADFeBvrAAAABmJLR0QA/wD/AP+gvaeTAAAD"
    b"0UlEQVRoge2av2sUQRTHP3cXA5IEtNPEQoOggmBh0AQLlSAo/gsxWqmNCsbGRgRFI3aChaAQ"
    b"vM4QG8HKOiGFRP0DJCbxBzGaJhhRvLV4u2T27cwkuZu9u+K+MHA3783M9zu78+bN3BXIH5H6"
    b"XshzsGKenTcCLUHNjpagZkdLULOjJajZ0RLU7GgmQV1AGXgLXGgsFT8iVVwYM3wqwN7cmVWJ"
    b"jQg6iogw/Y7UhV0VWE9QAZhSPu+BUr0IbhbrCTpn8TlVN3YOFIA+YL/F5hPUASwo+0R+NDeO"
    b"Z6wt5qvK5hN0R9lWgd48CLYDD4HXwEWgzePbRXpB/1J2n6BVZbtXK3EXbqqBPgCDDt8i8Ak3"
    b"aZ8gs/4z0BmAuxVPLEQi4CX2V2KY2gUNB+JuxSHgp4VMBPwG7pOezQIwvQHSLts06dugIvIq"
    b"B8VOZPf+ZyEVAV+A8waRftbWko20S1Albkvc1zDyCleAp+Rw7XUEmLQQM2d3IPYtO0j7BJXj"
    b"z/2kn3JSDoWTsoYCMER2zzBzrzIifsVC2iVoJW5TJpv6JP3mEsYTdCB7hw63SVkBZlUbn6DZ"
    b"uI2tr1/A5fAS7NgFPMc+q9VGObO8AvbkxN2L48CMIrOsfHyClpVtJu6zoSgikekbQuqWYWsn"
    b"K6jdsN+O634A1wiUYZ/Fvdg3WyrADqPvUYvPqGHfGWjcCJgHzhB/CNXpdzVZXyw+X5XPUsDx"
    b"50LfKehXRq8ZkI3a16YmFJFseiFQf9uR1yhB2eJj1nUD2wKNPY9oqRmluKNF5IlcN2ztyJr5"
    b"HJdR0kHhRtxmEbhEExy7bWF7EZn59dBDdv00LGzvBsZxL84Z/KJ6gHee9uPxGHXBNSQtsRFJ"
    b"Up8k4o2QFtaNvGbJk5nFnfqsImlWR55i9uFOIs3kVNuXyWYFyQT4ktMICVhD5PTreZ9lwGnW"
    b"zjNlZVu0+Ou6JOoNYD8+JGWSHC4fC8ihq4IcwoaxH/CScslC7KL6rg9457FvyBGyh42R3hqC"
    b"oJP0Rb8+gkfIoi9ZSJXIRkZ9BO9Ejvm/HcKWgIOhRZnQlyQRcCK26XqQ0KzrbZckvcjFjE3U"
    b"o/AyBJ3IpqnDbgKbIIAXqv6jZ4xB5CrN9B8JQz+Le2qgVdJ7iEvQbtLh/y+w1TNOG7L+XgMP"
    b"gC0hyGv0kj2O31U+LkEge1oSSB7nQXCzmCC7Z+jbT58gkL3tMDn/S2sjOEmW7JDFbz1BTYES"
    b"8qOUSXQK+yybB8i5ehHcLI6R3RyPOnzPIKLmgNN1YVcFDpDOCsYaysZAtQeqJSQ96QbeAFeA"
    b"P6FI1YL/vgFTqCh5LwAAAAAASUVORK5CYII="
)

# ----------------------------------------------------------------------
icons8_padlock_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAAAXNSR0IArs4c6QAAAARnQU1B"
    b"AACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAFqSURBVGhD7dXPKgVhGMfxIcUdKG5A"
    b"hJKyscFCFFaW1jYnW25ALsEV2CALC7KykLKwslK2SllIiUL+fH/lqdN0GF7nnT+n51uf0mSa"
    b"+XXmzEk8zyusTgxjGpPoRxcqUTsWcIAnfKQ8Yg/zKG0DOEX65r9zAn1KpWoOD0jfrD6BS1yh"
    b"0Sd0jxmUIj3/z6i/wV1MoAOW/p6CHq132P/q3HEUWg/uYDelv2eRlV4A9efdohuFtQ27GT0m"
    b"Q/htI9CjZ+dvopD68Aa7kSX8tWXY+a/oRe61Qd+PHZzpQED63uhFYGNqKDT9foS2DhuyrwNV"
    b"TT+ONuRCB6raKGyI3l6VbRA2RG++yuZDylauQ1agX/EYjmBDXr6O1dO1m9YW7GJ507WbVksO"
    b"OcZqZIeIPmRDByK3Bh/yUz4kMB+SlQ8JzIdk5UMC8yFZ+ZDAfEhWPiQwH5JVSw65wXlk14g+"
    b"JG8+pFFjWCyIru153r9Kkk8J85i7zVovlgAAAABJRU5ErkJggg=="
)

# ----------------------------------------------------------------------
icons8_opened_folder_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAAAXNSR0IArs4c6QAAAARnQU1B"
    b"AACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAK9SURBVGhD7Zk7aBRRFIYXLIKCEQux"
    b"ExEhYhcFCxEFUSsxCJFgAqJ2goWIdiJaiIrgI50kjRoLEdJpumApsfIBFpKg4AvxBYqF7/87"
    b"zFnuzowxu8p41P3gY+bc7C7nz+7cO49amzZtfspsOShfy29N+FSul2E4LWnsiyTMTHwrec87"
    b"uVSG4LmkqeVWzZwLkvfdlLMY+NPQDDbLPPlQ8t6jcn4Fdsof0moQWCc/S/+MKnwk+2QBf0Gr"
    b"9MoHsuxY+t36sck/b5Vs4FeDVM0xSb+nrEr424L0S/q9bFXCfxFkjlwSzH2Sfq/KBsqCMM1d"
    b"kZ+k/z2iL+QOafhgynnJGCv3ZFCZhr/K+gyWD8Iq/VLybSxkIDDHJb0zkxWCLJPU96yKzRFJ"
    b"r4co8kFYNakLs0JARiW9bqHIB/Gv66BVsZmS9LqIIh/kuqTeZFVcOGnlYH9llcgHeSKpox/o"
    b"ayV9jlsl0iALJPvPrIrNXkmvZ6wSaZCNkv0xq2IzLOl1p1UiDXJAsn/CqtjckvTabZVIg1yS"
    b"7G+3Ki4s2h/kR9nBAKRB7kj2m71+rxr6o8/bVmV4EJJxWkLSEDcTpoFfDD1ftCrDg6zIthMy"
    b"Oiclve63KsOD7Mq2QzI6zKr0usGqDA9yNtsyP0eHdY5eWffqeJAb2XaNjAxnHPT52KoED/JG"
    b"cu4yV0bGF+1rViV4EOTKKzqcldOrXUylpEE4v4/OiKTXwt3GNMhhBoLDlSu9dlmVkAbpYSAw"
    b"vmi/l4VFOw2ymIHArJT0yaOMAh6CWSs6uyW9cruqgAdhHYmOL9p7rMrhQc5ZFRtftFdblcOD"
    b"8LVFh58/zzpLF20PwoEUGSYi+uShUikk5AU8po7MVkmfhbvwzl3JC7gbsS2oA5LrJPrksUIp"
    b"m2XVDzRb9b6c9skudyK46mJ+jip3eKKfmbf516jVvgPWjL2OHf8X/wAAAABJRU5ErkJggg=="
)

# ----------------------------------------------------------------------
icons8up = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAAAXNSR0IArs4c6QAAAARnQU1B"
    b"AACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAADySURBVGhD7c9JCsJAEIXhrJ2Weg/X"
    b"jkfwIrr1MJ5FcDqCHsRh4UZ9jRaEkEokdsdqeB88aGrR8CdERERERBY0sP77GS8XscbO2MAd"
    b"YiQRz8+ijMlGRBmjRcgumPmYsgiZixliJmkRB2yJPVI3N5MxWsQe62DOAsvGXDEzMd9ECLMx"
    b"RRFtLI8WM8L+okqEMBOjReywsgiRF3PDaovxESG0mDEWVFFEC6ui9hgtYotVjRC1xYSMEFrM"
    b"BPOiKKKJ+aTFTLGfdbEjlv58g/mOENmYOzbDvOhhJyx0hJAYrxHCxayw0BFijnmPICIiIiIi"
    b"olxJ8gJfK6lldYiKtAAAAABJRU5ErkJggg=="
)

# ----------------------------------------------------------------------
icons8_usb_connector_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAAAXNSR0IArs4c6QAAAARnQU1B"
    b"AACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAMvSURBVGhD7ZlLqE1RGMeP9yuKJPKM"
    b"DBSllJC8MiIkMUAZkFeSIhOPDKSUgQETjJSBMvEoEga4pRBFCil5JEKSV96/37l71b7bOfse"
    b"g3Pu2tx//Wrv7+zT/v5nf3utb61Tatd/qO0wuvmwuBoGH+FE+azAOga/4CdMMVBETQINaESa"
    b"oAMUSiZ8DTSwF54nx4ugUFoOJv4EesKq5PwBdIFCyMSfgokvM4A6wV0wtsFAEbQLTPgWDIGR"
    b"CevB+CvoA1FrKDjcmnAeeyBqHYS34K/+CEKJfU7OAzehNxRG40AjV8pnLdUdQtlVYiBEozwj"
    b"UyGUWiXOQDSqxUi27F5AIY1kP5sLDTUyCPo2H1ZV1EZmgTO0N7OXugijoJKiNTIdQiP4Gj4k"
    b"xy9hAGRVi5HrkB6tVkLdjdwBb7IDbAxtR04lsQOQVS1GqlE3I73AGzhzdzSQaCIYd5LLKs/I"
    b"eLiR8BC87l0qth/qIpP/BN+hv4FE88EkzpfPWirPSFoNH6mOgze8DLNhCdiqG7MpzKpWI/Og"
    b"oUYGw33wpmlOQ2fIqhYjPt1z4HV1K6dKcu7YDd7YUWsFVDKh8oxYquvAJtNrHPmGQ0Nlu+7N"
    b"Las8VTPiet7Bwc/EJ9pwE6obOHr54lvf1ZQ1YhkdgR9g3N4q7/sNUSgvJ0jnkB6QVTDSBOky"
    b"cvRzJVnpOw2XE+ImsHs1uXswAdIKRtJYRtVamjbVWLgNJvkVtoGbDSptJIoyak2+M+5fhdq3"
    b"lPzVgxFbmyjKqFZNg8dg8u9hX3Lc2oQYpdzqOQoaCBTSSNBieAOFN6Imwz9hZAZoxFm8UC97"
    b"0Exw5RfeEXG+OQT9oBBaC2E57I7jBfAvhm9JzFFtBEQt3wn7L9kC6a7Yv+EugWZ8WulVZnQ6"
    b"Cya6s3z2p1zjh2XtQgMxypfZFuUL5G1QbwSNHC6fRSjr3gT9xfPkQOB1ldb4UcjRyARt1fPq"
    b"fyl4nev/aGUrb5J5Xa4bDF5jiUWr1WCS/os7xkBGW8HPbV1a2zduU7kOOQkm6yrQCXANbIar"
    b"YNyheQFEr67g0jdMgGmewRwolNyQ9kloynWJ3XAh+612/b1Kpd96WyDV7qTTNwAAAABJRU5E"
    b"rkJggg=="
)

# ----------------------------------------------------------------------
icon_meerk40t = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAAGQAAABkCAIAAAD/gAIDAAAAA3NCSVQICAjb4U/gAAAgAElE"
    b"QVR4nGy8Wawk6XUmdv4l9oiM3Je7L9W31q7u6m51s7mIpJqkRGqGoiBpJHkkeTDSAB6PBvCD"
    b"AdlPnmcvAwMW4AfDDza8YCCNOCPKlEVSHKopsnrvWrq6uqpu3f3mvbkvsUf8ix/+qmSxx/lQ"
    b"yJuVGcv5v/Od75z/nEDr6+sYYwDgnEsp1XshBEKIUooQ4pxzzgEAISQR5EgihDQmdaoB44AR"
    b"lxJpRAghAIgEhBBCSH0OgInAOiYsLzARiGDOC4qJAJlhCQAak0iCoFRgJEAKITSEJRfqIEII"
    b"dV71rxBCCKHruhCiKApKqUTABBANC5lTAD1DGAjW9DBNbNtOi1RKpC5bIoEwY0Jgjp98KKU6"
    b"IMYYY8wYk1IihAgh6lyMMWUHAJBSAgApl8vqZ+pv9ZJSEkLUe4SQsiAASJCUUiQBpAQhAWMJ"
    b"gAiWAAghgjFGCANCT48uQSKEEEGSc4RBIiSRxIgIQIAJwqBLTAAJLBHCUgICoITA0ytRB1lc"
    b"rroT9V7dIRccA8YEIySxBCoxSMRAAiUCCca5kAIkAimRlAKE4IIzjhBeGEtKqd4oGy3O9SmD"
    b"qBdVOFKXog6xuMQFvtRXOecYEAHEJSBCOOeYYs45wlhKqcyJASGQUkoCICQABka5wBJ0gSUQ"
    b"hCUiTCKJkESIAiIgAAksJRdAEQFE0NNLRE9fGGN19eq9ulpCiBAChBSyIFgDhDgTBQgBwFhh"
    b"OFbOc4Y4IEASUYFBIikJCAAQ6l6Uu6iDK5wqUywsqK5BfU29SLlcVmhfOKAy3OIbyoKLqxec"
    b"gwSCMcJP8akWREokASOEF79FCBEMkmEMCEAiKTESAiSigLGUgIQkgiMpJQaJEEiEAEuQi5Vb"
    b"vACAUso5V+u/WEuMMQhJCQFAAEhKAISoqSOKcpaBFAQwRkC4RBJxRCRIjFFRFFJKTdMAIE1T"
    b"hJDneerDTxnrU+CiylKfMoqy9xOoP+UyjDFCSDCOMZZcYIIFFwRjkIAAhFT+hzkCqT5CCIOk"
    b"HLDkktAcSQZSYkSEpIhIJEEKgQCBxBIAhJRUgAT0M7/7FN6FEIt1XiwnIiARCC4wxgUvEMGG"
    b"pcdZCgXHAAi4BMwkSAAOmAGCgum6LqVcmAkAoih61jEXFvi5EyFEnyXRBXwU2pV11CEW31Fw"
    b"ZYwRhEBISgnnXN2hotKn7KbWRS0RRghhCUhyJCkSEhDGSCBEOGYIEAAgQBxAIkBP6ekJNAlZ"
    b"ELCClbqHJysnBEKY8wKAAmApJcFYSpllmQYYScCApJSFlBIjKSVIpOl6UWRCCMMwCCGc86Io"
    b"1M0+60AL3198KKUkpVJp4YOfWrT/308QJU+4XNkAQGIiAQmMACOk/GHBlIAKQrmKEFxgACKR"
    b"5AgRxIUQIJHkkiCBEJcIECCElZ0XR1BXyRhbfLKIVuq/EEGMM10zMCCCkWEYrMg5YxJrIDER"
    b"ABIYlpIQggmA5KzQKDEMAyGUZVmWZcolnyWfxZsFup+44bNm+tQ3FObV2iobC5BCIJ1SQ9dY"
    b"ngshcsawpguCpFo4CRgQlgAAAiGBAAGRIIVkUgIBwCBBChWZEQJBkAAAEBIBAVC4WLieECLP"
    b"c855nueGYShCME2TMRbHMaUUY2w5dpExkwrJJKaYYhIEGSEESSKlQBwJxAUCjCSAQIJblqFk"
    b"gdIKykwLbaQs8KxieHbZniipxXIplC0ihfrep8JlkmWC8HK5PJ+HAiAVhUZ1xrlBKJYSOHds"
    b"K4oiamiIGEUOCOM0LWzLgDStlEtJmnvlGjWteqt5795dJtl5/8w0TRPrmkWLgjHGiqIwDGN5"
    b"eRkhdOXKlRdffJExtrW11Ww2syxbW1t78803Hz16ZBjGn//5n8uCT4cjy7I8s8SLQiMUOBCE"
    b"kCQcOAKiYcw4I0i4JTdJc7UAC7aBpzHxUyypgLLgdABAKysrCy36rGhYWGrxSwAAjKSUlNIi"
    b"yzVNo5oBGgmTGGGsUSqTnHJpG3qR5abnzKJQN5w0yDXD2rm6Vam6lzbXl5vtPM/DKLFLFUGQ"
    b"4diO587n08P9gwd373W7XcuxNU2rVqvf+MY3Op1Oq9UKw7Ber0dRZFnW7u7uxsbG/fv3x+Nx"
    b"rVaTUh4cHL3+2me+8+2/GIyGf//WzSRJHMvNotjAFGMc5SlQwhG3DN3AKEmSjAv5hD+eCIhF"
    b"+HrW6Z6lqp8Za3l5eeGJi7jzrHUXOISnYrVQq4cRY8K0LKJrcRxTQJhLkxJCSFrkYR479crW"
    b"9sVf/+VvCc5Hs3E4n1y5dIGlyf7uY79UGQ6HS5ubkyTe3nmuYrnT0RADHB0dbF3YYYJfvHix"
    b"3+8XReG6ruu60+mUUvqjH/1I07T19fXbt29fvXp1fX19Pp9rujkcDos8bnXaN299+O/+4tvZ"
    b"NCCcszzVTD3IUoRxqVTO4gQXeRRFuu0yQM/qA3iqcp+1y7OAWngoKZVKC1g9+0b+vDj82e+E"
    b"pIQQQgTnBBNWFFiCTXWDUFnkjLGc56P5ZGVz/Ytv/NKXv/zF6XRUb1bvfXxvZWn59u27hmkl"
    b"afJ4f7fRbHV73Wsv3tg/PEBcTsYjKUS57DMutra3dnd3m80mxng6nU6n06Ojo+FwKKW8f//+"
    b"1taWpmm+7xdFkSTZxUtX0jRptOqVemU8m3/tq181Nf3ezbdWudw0TFenjm0OZnPGhRBcNwyB"
    b"McDPMKEY+T/mdfj5/OGJHZaXlwkh6sfqDef8P/794k+CsHJ4KaWmGTwvdEwIwppGqK4NZ5NG"
    b"p/mf//G/sCzD87w0i6I8jKKo4Xf2dg8P9o6TNF3bXn304P6039+8sO1W6n6lWi1XKEiKiWub"
    b"luMxwTVNs2371q1b0+m0Wq2qdAQAXnrppQcPHmiaZpqm4zgPH+4udVYQls1WOY5j2yrZrvPw"
    b"4ScrQdL9n/63Vcv+SM7/rzvvDRuNKSUYYykEy5hGqGKrZ9X5p8z0rIhf/C/xff9TCFr44Kcx"
    b"9TQBzPOcGBoimHNBELY0I01TwJBK/vqXP3/l2tVrly/NBsPzT3bXbdcaDcb7h5mQh+f905N+"
    b"tVp3S6VWu/X5L3wWpBRc1KrVw6NjXaeC8ZW1FUyopmmz2YwxVi6XK5XKeDwmhBiGMR6PhRBh"
    b"GNZqtdlsVq1Wi4K1Wm3fL2kaTtOkUa4fPHpccexNJvl3vr+ZMdvSj8eDY8nmOiVUL1KuaxQj"
    b"/Kw54OeV+qfM9GljPctw8DQ0fEp0LCzIBdctkyMoOKeaDgCcMaJrYNKrL7344msvv/baa3sf"
    b"ffzKxsUvbl+bvPlu7//4t5vEYJ2mqFV9u7a6vP797/3NpUs7w2l/bX0lmYdxELZXlh/v7Ukh"
    b"HNtqtztBEIzH40qlIqUslUpCiHa77bouQmh7e/vhw4eMsRs3bpydndVqdQy43qgVkHc67f5J"
    b"b7XapPNo+NZb1aNDn6WYiPM87dVKY4RsaeoSU0qF5IyxRUCEZ9TSs5b6j/UmUVezkAgL6z4b"
    b"FDDGSqhIAE2naZEJCZRSzgQGIBhyzr71W7/5m//J7wwns7Nu98bly/FR91q986P/4V+/hmj/"
    b"8OD1P/z9292ua5QIpl/8wufffvcmYHnvo7ufe/X18+75jZdeoZRolCAsR8OJRHD9+efH43GR"
    b"5aZhcCFs2xYgJ9PJxYuXz7pnb7zxS75XajbrIGSj0bBse2WlAxKSJDt7uPtyo3n0ve9Xe+du"
    b"nmgI7OXOXSFDy4GCZ0nMBONCPF179FSiP+txQoW6Z3J59BRZlRLBSEoghHABCBMhJMFEiUKE"
    b"gXOGKeYgEEYCBKFY1zVWFBrGlm6wPA+i+R//yz9eWl1+tPt4qb36pS98Waf0pfVV/N67wTtv"
    b"11maAHNvvPDKG2+89MINx7ZXVtcKXrzw/DXHsdvNzqWLV0XBKMa1ur9/sK9Z5qVLVziTQsg8"
    b"ibM05YJZtpMJrhnW5SvXoiDyXU8jMOydEQLNzpKUosjyOIp119lptWrD8Z3/8/9eFtjlQmPF"
    b"MGdf+S/+yx/evUc0cH27YFkSx6ZpcS4p1gQXmGqMc0KxFBwjIBiElIAlRkgIrkymPI+U/ZKU"
    b"EkCldQghBFICCKnUGkGEEELJk0KVBMaFrhtIIBAAjF+5fPlf/vG/WF7prKwsv/LSLxCpGZph"
    b"2+YSQt1/+2384JMygYygAaGXv/Tl3ngcA+KSb13YPjs/QRhZlvfchR3OmOs5Kxury6vLB4dH"
    b"UoDve+PRpCjyleVlTTdKvjcPQr9cmk4mRZYVec6KIpgF+weHzaXOZDLTAbfbnVSwDsWj7343"
    b"vfWBR/JOp57OZplp3+wNv/67v7t1aft8PJiPp0TTDMMUEhREWFHohg4g5RPHQgghhDWQSJVU"
    b"Fh5G/JInhOAIcSEoQlIKJKUUkhACWCo640wCl6gQRGJCDYRpyfYd2y3ZpRdeeGHQ79Vq1Uql"
    b"IgsZjkPHMGv1isfzv/2T//qaYcqiYFR7dHq2cmGnK8T+dFKI4qR70D3rttudOI1n8znWtOFk"
    b"GqT5rTt3r1x47uz0tOSVoigsuBAgEIAoimg2ESznLIvC8LR7pulOEIiNjYs3336rXq83a/Uo"
    b"jgTBDSlGf/Zn+tnjGPrtr7x2/tGuMEpzhJ16fenyxa1r1yp+9bx7XggI4sg0jSQLkeAIAWec"
    b"EKpjigQRknAGSFBdsyQSUoqnxvJLQghJiJCCIgziichCBBTKCCFCAiWEYqzrpl+tzCbTql/b"
    b"WNnY2NwqV8qf+8LnZrPJ+trqdDwydCucTgyeJe+9h376Tj3P3KYX8oxIkgAe1+t7cVCrlQtW"
    b"TGbTw8OTyXjywvXrURTuXLy0t7+/tbnx+NGjWrV63uvnrNjZuZjlBSU0TZI0TmrVChN8NJ4M"
    b"J7PJZNpsdPqD/t987/tUI2XPK3m2LIpKGL/z3/3rNk60Fq9cWkHjOIxFwuTqxYsf9Lr17e16"
    b"vTmeTGfhdB7Mmcw1QnSNSsERpRKgyAspJNV1QnTOQYDACCH0RIESv1yRKihIoBgAJCYYYRBC"
    b"YIQoopTqEhFJiACQGP3CKy+ur608f+X5X/u1X3dLVSah3q6H8dwmmu+7VsWxKFyteJ98+9+5"
    b"e0daPq987eWTh3cb0n10cvYusN08vrix8c7Nt8u1xnAw3FrflJzv7+3pGt59+IlGSLfb9cqV"
    b"w5OTLM9ty07i2DXtQX84nMxXNzYf7O7vHh19cOv9IJyF4ShJw/FsrlFiWebbP/67O3//95Ob"
    b"79Z2T1wZV58vG1VNi0XvbKhrTiDRrFXtCb66upYV+d/+6AccCss2MEFJGDqOm+QFooRijDBC"
    b"QjLOBBJUIwAcIXjCWaVSCRBSFc4npI8RICSFxAhhwIAQA5AIABEE8uR4/1/9q//mF155RQCK"
    b"stS0zFk0vXrl4g9/8IPW0tI8T808XbWdv/tv//tlxqoVzXx5JTo9cOeEU+cHk/O84nUPDpFE"
    b"pyfHWZq06i3bdqbjked6nBVCSp0amJJ5EDElRCUYVNM0bWll6fH+/sHx0Y/e/DsheDCfLq90"
    b"Dg8e3/vo3mAwvHX7/cHB4fjOx87J+SWJZNpf+sIGaAkut84+euSCLUx7z6A9ySqVmq7rN9/+"
    b"aaVaDsPAtmwNEwC15yIl4xghTSOYoAKxQuQYAQKkMmXilcoYsBQCSyRBYgJSCgCJJCCEKKYc"
    b"EKYapZqlG5TgS5cufv1Xv/7RJ/dSXmBK7tz+sFaxe4Oe1PSVzQt2qdIGknznr4u7t8s4X36u"
    b"DlXu6iTZmzHNuxWP9ieD8TzIeD4fDSb9Xnu58+prr08mgeOWwiTZ292PJ/PXXnn1//3bH25s"
    b"P5dkuWFow+EZRlw3affs+M7tWwd7+zwvLMt8/Hj39q0P8yxxXXPQO+/e+4QeHX11daOeh2Vf"
    b"uld9SKZADd6fknEyS4twa91c37h//97Ozk610njwYNcy3DzJ/FLJMPQ0zQCQoRka1aTghcwK"
    b"PReaoEAJerJ3Q8p+GSEEQmACEoBQLAEQAEaYYI3oBhcCUwpcABdFkv5Xf/InJ92upmvd89Nq"
    b"pXqw/7jZrJ2enEqgo9n84YMHm0QLv/s9f3DOxKT5+kVwYmJqwzsnulvtY/4f7j4YRQkn+nQ0"
    b"Ou+dJ1mRZGkcpcPR6OrVa0mS3rj2/AcffHDtxRdnsxkI0W63bFM3Te2TB58cHhzevfPR8eFx"
    b"xff75/1HD+6HQTAezYe900lv6GfZr5Tbr5ZLNBmtXyijFgKNg8RGgYrzNANrUq0Ulsm4sFzv"
    b"0pUrr7z8C7pGXccenp9zxoVEIAAjSjABISUWEgsQ0iAmhifJH6lVahghEJxLjhDCBCEhDaIh"
    b"TCQgjpBpWyXbRnmhMXl5+8Jrr36m014aD3vT2SRLYtdzBIfJeJoF0d7DR8FsGH18v3nn4RJL"
    b"9KbwrzaFHCLXjQ+HScbcav39k7NhVOwP5+eDcSFks9W88vyVF156XgjePz3znZKUwnTM4bDv"
    b"ulbJcygBznkUp17J/+jOxycHp7PxPE/S6WhEERYFIwQIB0NAG+Afmv5lCknaa33uEpAp4Bw0"
    b"Qr3O4Z0BojVwTd209ruDytLKJJiWq/4Lz1/97X/0W0SSx7v7wJBumIZlFoxRRCiihGGbOhiw"
    b"quRgjInruAghTdcQBsAyyzJbN6REBROIEialX/LLbilLIkLkf/bP//na2vp0Pvvg7m0hRffs"
    b"lGV5MBilvZEdJUdvv50fHqwH8Y0MzHzmXbKNNuY4x1nuYm/YnxvYHZ/3QhCEgUU0wYokiRzX"
    b"Wl5fnc7nL11/YTaeSIIn8+k8mF65cnE6GZ2dn21ubecFm8/Tj+8/GI0nWRzprKhpOoqCioS6"
    b"gE0JVzT7myubX213cNAzG7h0sQ44BFxIAIRsPuTxPOdpLMPYN2yYzzumUSLQsKxkHrz62mfa"
    b"yyuzeSgxns1nUvI8SUBKHRlCCAlIwpMtCFKt1BzHSbJE7Z6US36aF1TXDdtiAkq2wws2HY9e"
    b"evWlf/jbv75z/fJHd++MZqMHp8flVh1TEvSH5iyOPn5AHz541TQ/i61LEWswmeFZ64tLwgyQ"
    b"TpHQkVU/uvXYFd6l5taSptdkYeQxKXIOvEBo48qVSThvVqqEoqRgTIjnnts+PjlcXl7WdT3L"
    b"JNHNB7t79x5+0hucFvFsydK08XgN4CvY/KONjT987vIbldYOoXg2CcV06aWO1sBAMzAIAgGF"
    b"oFEaDsZWgmqxqPb75uN98+zUGk0263VT09/96GNarRDHfv/ubQ2BZRBdQ4TIKAmFEIBhkWRT"
    b"XdeTLDYsk1KchEGapkAw0vSciUqlIvJiudP+w3/2T2vtmkBcR7IM+MO33t3yrXJvmPb6mwKC"
    b"h0fXNKtWq/h54sShAyJmKa4DOCCpLNLMBB20wu/YydnAMcVnGs7VpfKE6OeA3+92Ucr4W++9"
    b"cOVKIwgnYaJR3XLc27duCeB+uWLqRqdU6x0cf23n4vDv3wxOumu+e7lc3llZv6DZjSytZDN9"
    b"uBfEEejYbPidrQ3juQrIIZMcFYxIAXphXW9eMLTRfjw+2q3oZt2wZr1gPDj5uw/fE0vLsL65"
    b"H0V73ZNv7ly4d+/+JEmmQs7z1HBtVggmuEoPOedoe/s5x7MHo5FOsUGJlJJTygH5dsm3SyXb"
    b"+vwXPvsPfuub773/9vWdC+Fet7h/Jk/OR4/umMGkKbg2T6p6mScJpmkuxrkWI4OtrK1Ury6B"
    b"PU5FZFIXMglAICOzR7PjR/08k5TbpixRahcaTSmJJNB2Z/P11xtvfAlMfaTh79/+cOXSDhNQ"
    b"081sb3+Fw0ff/e7ko3ulvGgZOkojW8N5FAOOmBg5FbS2s6RvdoAwQAVABhpiIKTkGnCZc0RM"
    b"EBogC5gePjwORln3cEKl7WjlrACgeka1IRFzzeLl+g8P9z8Q6USnUZRgjDGgRS8IWl/fJBo2"
    b"bZsXWTge11vteZaZjqtx3KrUXnzh+RduXMceXW/U63G+9703szt7tNttyrSUhk0E+WyONZqI"
    b"qL7V0Fs63a5BiUCeACRgFIAlSzjVDRA55AKQB7QMCS52e7yfn++embqdZ8I0y3OinQE+B6hf"
    b"u2i/eG3lV79+dzySmtECNPj+D+c//Wml19skxCsKnGcIi1E4qq03aleWYdMFPAcxB40VLKGU"
    b"Ss5BIqbpvGAWxSBFDhIRTAEhSQC5kGCgLdjth7v96eHQKrBuOnNKI9MZYuvEL/37ZPxhPEs5"
    b"IlTP0nhRkkFrK+tUJxln5ZJbc0qTyQQ5NkJkudxcbnfcshtl8atf+IXnyzXr7Qe7f/btZRnX"
    b"QehFriGpG7iyUYe6gK0KFGPwNJmnUhYYBCQBuI7kDBEKRQEYA0GAAPICkAXUhVwDrQJ7YxgV"
    b"4/1xEjCGdKQZWVY8NLD3T/8x3HghYNLsD8Nv/5X/8OG2KOw0JoSEedDeXKZffRVkH9gQcAyU"
    b"ySIHzBElAAKQAEAcU8aEzgFhIoFJyTGinDFMCZIaZBpACUgFaB1+8O7wYIBNl4OWMTJo1L7r"
    b"sL/YezgTmjQsLtmiUkia1YaUglCSZaksWKVSo4ZuaAYwUWT53uF+xvLllfbF1kqn0B/evFky"
    b"pCxiHVOQkPIijCdMBroIcbsOWYI0EzEBLAOdqu4H4BwoBZDAJRQMqAmCAtLB8JKHB5OTwfhs"
    b"Mo8TTnSwrCAtcgnnUq7/yldTz6202h7VnCCcnJ7wLBUaiQhI05gk0/13f4rCgU0AV1oAGkIE"
    b"CQKIABcghQTJOdI1AwQgDAgw4gSoi7mGwADiAC3BUf/83v6DH97MMpRTOzasKdGgVDqj8v35"
    b"cIwQo0bKOKE/6yZCWxubVNcYY6qXiDHm+SXf9yt+lXMexyFg9K1vfdNCaLvUSI+O5g/vuKMp"
    b"OerVcuaLXM9jInJARZAHpWZpeasNDRuaFqAAaAqSgYQnzTWcgKhAgOTxqHswnJxFruZaGKcA"
    b"c4OMid7l9MJnP9+4ek1bX3u7f5aWXLtaF2nKzs+dMIx2H0X7e36SNHjhhoHPUr2IRBoxIFbN"
    b"ru1U9K0GGBggApJIYAhrknOOGQIgoIOwQPoQAds7TwbBYK9nEpsQJyd25pbHun5E4P3zk1tH"
    b"h1NTsy5s5oYlMI2SbBbMf1YuvnDhAmNM07SiKAghtm1rmlYul13XPTg4yPNc07TXX3/96tWr"
    b"jUZj1jubHezVMrYljEc/+tFGpWQkicvBkgCS6TKDZJrxOfbh4mtbpI0lzSQXmBrAaXoaHr59"
    b"DJGOtFIBjqaVC4k54SFlSdkuX7n88rd+FzrLc5C3jx5LakzSpFSrPz7Yv3vrdtP3YD7f9ku7"
    b"b/74zve/9+X17XXbqiNcxhTSAkMRij6DoN1wa8uudbUJOAPGQSMMZzIHjTaCj3u9x8N4xDXk"
    b"YmRhpEcFLwwzNOyf7O99Ek0fABsD4Go5odir1k3bIQhPp1PTNLMsy/NcCEHUVqVpmpqmua5b"
    b"LpfVjnSv1xsOh2oz6uDg4OzsrNPpHJ10Hx6fbL14Y67RUcn+zsHjm3HwTjTbJaKngd3soESr"
    b"GzU9Fr3Tk/qNbYQSZCAACqL08Id37dQBXB2YpXG1eRfkD2aDv44Gh8v1pW98XT536bAQqWnd"
    b"O3qMdOqUnN6gV69Wfc+plksHBwd7B0fDKG5fvPThSXdPwj0hPqL0bp6zqi9tx9J9l1l0nM3O"
    b"+46NacUCTDgwIFwTRnEvObh54uY+luWBcM6t0kPHWPmdX7+/XP0fb//0A5TvUplaNvHL8zRH"
    b"1BAAhOiGYVq2kyTxz/bNqtWqpmmqP6IoCsaYaZqc836/H4bhaDRSOxqGYezt7Tmu+8prn3Vr"
    b"9ZVLzx2FQez5XcH6kp9k0cOz0/3+kCEbC9xEBk7D8oYHWpaxlAoNztBwdyZRdWL6b4fxj0fj"
    b"PUqGNf+0ZLY+8xlvY4vUW8LyRnHcn4zOhwPLcRqNxmg0jKOoyPNyuTKeTVc2NkZJWtvaetAf"
    b"ZH41rdSO4uAsnI/S9HQUmnqpabkyTVMRl9ZXAXLVl4VxtfvmMU7LM80bl+rX/9Fvb/yDb1z9"
    b"zW9NllpvTfpBrfJwMpkDFpqZMSiXq6ZpYUxynumWgSlmjKkWIQAgjUYDAPI8d123VCppmoYx"
    b"Ho1GSZLkeU4pnc/nRVHYtj0ej3cuPPeNr3x1Nh6vry+7rldvLBFs7h3sVZuNUTiv7Vw4MpBW"
    b"Ka1loiSSWA6dCy1KAbiTPkiGA5j59ffy9C0pxu1ml2Wd5y+vXr529fpLnukNeyPOeZzGQPV6"
    b"s3N21g+jmGg0jkJN09IkJhidnB63Wq3Nza3NrQvzIHy0+/iLX/3KBw/vh7b9kIvDYFahxDf1"
    b"cDZvX9gCGiGcITBQ5sw+HOZG48FyZ/Of/ZPJxc1Jpz7VdbPR8MqN/+V//l9Lpn/98vPzSbC+"
    b"tjrsDxBCUjIJwnRMQJAlWZ5laZoyxki5XEYI6bqOMVbIYoxhjLMswxgrFiuVSnmet9vtLE2/"
    b"+IVf9H1PgqSGYdpep70UxoHtWmAY/SwtXdh+7cZL8MljX+YBn9a2l4GnQMuHf7uHtdaeY/40"
    b"nHf9kr667DXqO1evXXz+xc7SSjKLmo3GSfc4L3LbcYfD4eHB/tHR4dl5dzIeI4QGg9777793"
    b"enpCKOksL13YviCkHI6GJ2dnIcunUswojdO0VBQb1borkAcp6WhABCL+6G43Py4GYOFfeWO0"
    b"vXGKud5qSE2PM/bOzXe//Iu/1Oks/eW//w5nLMtSSggrMgm8EHmpWpZS8IKpxliMMWk0Gmq/"
    b"VwihaZpySc65pmlCCMdxbNtO09S27SiK3vjKG612u9ps2iWXmobtOH6lRAkreaWdS1edUvnF"
    b"ay9fX93Co+Fs2IU86bRbYBEYZ/NbY+K230HFe3Hw/Be/7FSqrUr9heevbz93kTGm69p0Oj7v"
    b"nyZR+PGdO+fdk/PuaZYkvfMuINTtdo9PTgnFtmMDkpZtv/LKS4atDUc9xzVNy9p7fNCs13XG"
    b"o97o+a0L+mSmy8S5Uoc8BVYe3TomsXGOjJXf/e0TnVx4bns+mZiE6ongM3UAACAASURBVFRb"
    b"31h/9Hj33/zZv8EUu54DSEwmY0SBaJqma6VKmVIKXBq6YVmWbdtPdqQRQpRS13U1TQvDcD6f"
    b"c85brZZlWfP5/MaNG5Zl7ezsjEaji5cu1hr1QkohIYkjnYiy62JCbM/vtFeno2lw3qtiPD/r"
    b"eoWoCElXmpN7+2RsTWjpr+bDZGM5wrjZbOlEf/mlV9I8FYIHwXw6GX388b1gPndMXfBC14ht"
    b"WZZtTydzLmSW5VLINM+/9ItfqtaqGCHLNpuNuqZRIUQSx/v7e2XXmc7nLdfbQaQYndQu1YAQ"
    b"mOmnt04FdqyLV40vfc65cKF3fOzquqkbmOKyX7l05VKeZ8fHRwAySZJavW47rm7qpml5Ja/I"
    b"eR7nWZYlSZIkCanX6xhjSqmu65qmcc4ppXmel8vl2WzmOA4hJEmSV1999Rvf+Mbv/d7vAWAk"
    b"iUTY0nSRxHkSaxSDxK5XSeOs0WwZQtYM6/z+w04BcjItPX/t5OYdkXvTcuN/P3xELj33wssv"
    b"UU2/dPGSaZhEoxTDw0/u3frwA5CIIGLahpDCsm0B4Nje8vKqaThFzoN5bFue53qmaTuWHYZh"
    b"uVQ2DN2yzCCYBrMpR5LWaslg8EXPL+czzeW01oZjNjpLR4J6L72Ybm08HvaXq7UiTommhXEk"
    b"EZrP5+fdXpFkLCsQwkEYMS7iOM3S3NEdWUjBuZBSgYnU63XVzLboDVFtlgghTdMIIbquU0rf"
    b"e++9Vqu1trZWq9WlBMu0JBcsT8p+yXU9ADSfB5VaxXHc8XBYFBmN4kpvaEeJR0jvbEL9pb/v"
    b"9Xd939za8sulC9ubJc/XdT2Lw363W+TpbD7vdFYkoCxLbcdeWlop+RUJOI6zTx48wBiblkUp"
    b"DYJwdXUlzZJ+v8cYG49HVNOuXr3y8e07WZ73o8hI0i9XK24eh3zmb1wM3j8OM+MQ0e2vf/3M"
    b"MVYuX6ZA8qLIBa/UGrppdM+6gonpfDYYjSeTaZJkSZwgQLpueJaTpUlWZFmeq+1+rFJqVZAv"
    b"igIAVOPdfD4fDAbT6fTw8HA4HH7zm9/87Gc/6ziO69q2ZyAETBQSkUkQ9MdjhsTa5lK5Yhcs"
    b"Bs8I6s68YkksHETHD8+wUTkhcMRz07bf+MwXlipVDbDkYu/RLioKi+IP336nXilvX7hwcHLa"
    b"7Y80zS35DcaRJDQuMmxocZFgg8RFZJXM0Ww8nU9qjfp4OllaWz8bj2fz6PrFq1XbK7ueWfZO"
    b"eDHR9WE/Ba0xOhzlHNs7O42XX75w5bqmm9zUccm1fD9J8+k8bLQ6DMO1l168+Pzlcq0czKe6"
    b"RgydOrapO4Zm6/zppiHGmNTr9QVnqR5eAIjjmBBiWZbjOJ7nra2tua7red7q6moQhQAQRRHG"
    b"2PNKlGqO45mmLiUvlUogZLVWn/HEzlPjk4fVgnMGoWYc2NrfHO197Q/+iV2rIMw1SqbTWckt"
    b"9c5OBeOWaz/c3bt17+OHj3alhCIrPvjgg5s3b773zttHx0dxOOsP+oah3/3otgRx4bntLM9z"
    b"VkiA8WS21FkJJvPVerPVbHzxK1+90GktgyhGI09q1X5YBHyENf9rX2Pb24MsC1nBJDdsazSa"
    b"zII5pbTbPQGM/+r/+c5Z9/T2rQ8dy6IYFXkmQRJKclYQ/KSszBgjvu+rXVXTNJVWQAjN53OE"
    b"UKlUStPUNM0XX3yx2+3W6/Xl5eVGvQ5AOEjb8YjALBcYE8aY49hxGBVBdt7tSYocxsrjIO33"
    b"LayFGrrva5/9oz/wN9cH0QwIcjzXc73JdOr5/sHJySSIjk7PPrp7P0+zfu9s99HD/b1HRZbq"
    b"Ou6fd+PZNArn4Ww6HU8Nqi0tLY1GU9fxdMOkWPMMz6YGwmJrZ9v2SpuNxhsv3bj9H95sCYsP"
    b"Io2QEyKXfue3dwm4tZpt24TiKAjyLHVsy7Gtkuf86Z/+6Ucf3cmSuFmvIyTjNNZNfX19DYHE"
    b"CBUFWzQik3q9TilV6SGl1DRN3/c1TTMMQzUFn5+f//jHP97Z2fmDP/iDVquFMS3yPMtilhdI"
    b"Ytu2mRCaRhkrXNczsSEQEEvb7nQuN5c++PFbDkLngj3/R/9p63OfyYCeDYau75uWNeoPszRP"
    b"s0Ji7HjenTt3DM0YjfpBEAjBNEIRllmcrK2snpx0CQLG5fbWVpqmrVZHCFHyvCxjrXrj44/u"
    b"hUFgOGZ7dRljUnbcoN8fPz5szLjL8RyJdLW99fv/mC91wiicTCd5lrKC1ao1goll6pZp/uLn"
    b"Pz+fTAkmnPP+YCCEMEyTFUW5XC7yPE2zRd8pdV1X13X0dEaHcx7HcZZlURSFYZjn+cbGxu//"
    b"/u/HcXx2dmYYhqlbjOWTYU8y7ji+Wyr3p2MhhEXIgDEEmsTCccxZEATNVrdSteZRbGqXP/eV"
    b"t2bjPJV1vxGmLIwmRZQEs7njlbrdbrPVqpRdkDzPK4Peua6bUZ50Oi0w4PC0SwxjHmc05zsX"
    b"Lx8fHo2HI9u2j/cPpZQyy278wvN3792PJWJIH45PvEZj5fLl6vPX04MfCoyGlK5+5vWzyehh"
    b"7yQYT8vlcqVSI4Scnp5mSVpyXdu2b9+9++jB7s233zIs07As3TYAaeVKYz4Oi6LwvVKcJqrB"
    b"mahuZc55EARxHOd5rpxRSlmr1UqlUlEUN2/e9H1/e3t7eXk5DKLxeJRG4crKSpqmx93TNM8q"
    b"lTJFVKc60WmYRnEaGZrOJa53lhjA0quvPkAotZ2D/f0giFrtJcZ4kWWWacZJsr+/f3p2Yhp6"
    b"tVq+fv36/t7hdDbzfd80LcaFphuAsK4bW1vbCOHReNJstAAkL4ovf+lLEoAQbDmOZtmaYXiW"
    b"aVp6iuSF9vKjv/5b07QfUbTxja/1LIOZemepwzkDjCjRhBCu49RrtTiOf/zmm7bjNFsdKYFx"
    b"keeFY9uu6yZhAiCDKMjyDAAopcSyrCRJlLyyLKtSqViWpcxnGEa/3zdNc3l5uV6vX7t2bXV1"
    b"1S+XHNcVUmZ5YVluuVLWNA2k1DSKCQYMpmGYpompbpcrncsXL37jlxuv3pC1MifIMM00T7ng"
    b"o+FwdWVpOpuenp4MBn3TMNvtzrvvvbe5tX3x0qVavVav1waDvq5RKcX29tbW1mYQzI+PjzBG"
    b"tXotimPP8wrGoihqVBonRycbm+umTpuNSl7ksUhcaozvHR9P4/zS5s6v/so5iFEUTCYThCnF"
    b"WhzHYRhatiWlNEyz3emc9c6Pj48eP96dTif1WtXUdQApAbhkiOBFdyBpt9uqhrVool8MTU2n"
    b"00ajUa1Wf/mXf/nXfu3XNjY2pJRZlgFApVKlmq7pehiGWZphhOM4xoQoSBY5G0+mw9lslCbD"
    b"PH086BPT4JzrhqHpmm1b1Ur5/Pw8y7LV1VVK6enpqaZpP/nJT09OTh8/fjwej8/Pz9UEhK7r"
    b"8/l8PB5zzofD4erqaqfT8X0/y7Nev6dRjRfywnM7aZGF0azsl+IsSXjGM7axtFna3nReufrB"
    b"4HTKC4mg4lcFF3GcEEIcx9E0rVavlXx//+BgNBqpWQQEKAyCer3u+/48mBWMPdsuSlZWVlRo"
    b"zPM8iiLOuZLys9lM1/VKpaLr+ttvv/3jH//4+vXrtm0r751Op8PhsNfrEUJc11XATJJE1X10"
    b"XXccx3XdoijiOAaALMsYY2EYAoDjOKPR6PDwEADeeeedIAg8z1NYPjg4IITMZjM1fCSlDIJA"
    b"6eTJZNJqta5cuXL//v0wDMMw3NjYyPKcUD3Js73Tw6TI4zi2bHM8GMdZNtNk1+BRxZSuIwDC"
    b"IA5noed4ruthQlRxhTGWpmmj0fje97734Ycffvzxx7PZzHVdy7LSNFWIYYz9XE8pxjjPc8aY"
    b"ZVkKXKZpUkrTNA3D8Pj4uFarfe5zn7Msa2trSwgRx/F4PC6VSrVaDWOsxmgAIE3ToiiCIFDo"
    b"U3rN87w0TdUNh2H4+PFjjHGapg8fPtzf3280Gufn5wcHB1LKpaUlKWWv11MiRhVCSqWSwtfa"
    b"2lqz2ZxMJs1mU9d1VXQzDKOz1CGE2o6taTQOw0/u3w9ngW5ZmUmFZ4VFESWJbTr1agOkZELM"
    b"ZjMJUrW/Z1mmadrdu3fTNJ1MJgihWq3m+76u62q0SjH4YtiEVKvVPM9VWiOfJkGq3jAajdSY"
    b"tBDi7t27v/Ebv6Fa0sMwrFarUso4joMgUJSXpqmaPAIA13WllPP5XEo5HA51Xe/3+/fu3ZvP"
    b"58p80+lUdf33+33DMNbX1x89eqQMoUq1jUZDpaXNZlOhO89zz/MYY5PJRPnBfD6v1+v1RvO9"
    b"d98ZnffTILZN0zQMyeVsNk/i9HD3gEpcccrn/X6cZtMokhgLzpTCFEKowsHt27fff//9oigm"
    b"k4myjm3bi0kV1ZSsckGq1k0BUplJeVaWZSqFbrVa1Wr19ddf933fsiwhRLVaDcNQCKEQVK/X"
    b"z87OGGNZlqmkUvmRmiEpiuL+/ftCiE6nk2XZeDx+//33v/nNb969e1fB1rbt2Wym6rHD4VBl"
    b"pmpaUhXX4jhWTi2edhnrug4AYRj2+30BstvtxtO567q9s/rSygo1ddd1TWpe2Nie9Id3T+9Y"
    b"Xqk/GDWXO6PJuOaX5vM5IcT3fc55kiS6rne7XXW/lUqFMTYej4uisCwLPZ2qf5I412o1xTiL"
    b"koNlWQBg27aatJVSXrp0aWlpaXt7O03TNE3H4/FkMpnP52maJklyenqqBoAwxp7nWZY1m82C"
    b"IJhOp2EYquXinN+8efP8/Pztt9/WNM2yrF6v1+/3Fagnk4kaAKzX6wgh27abzWZRFItJCiWg"
    b"B4NBGIaWZYVhOJvNGo3Gzs7OWfdsOh5vbWz4rut7pZW11VKtrulGOJ7lcUqp5pZKpmFU67Xu"
    b"8FyAoIAE54ZhnJ+fLwZ2Dw8PGWOq1V4lLZRSVVZQ/qgolVSrVcUviyZ4NY7HObcsq1QqGYYx"
    b"Go1ms5mmaZubm1LK2Ww2GAxGo1GapgDged7Z2Zm6k+l02uv1Tk5OkiQJwxAhpNbq7t27juMw"
    b"xjzPQwj1er2dnZ0oivb395MkKYqi1+sp3TsYDBhj/X5fYUpK2e12kySJoijLnkygmqa5urqq"
    b"qpIYQ7PZiKIQABm67pQ8apqnZ12CMOM8jKMsz9M0dUvO8upKrVKdTaaNel3BQoWmv/zLv5zN"
    b"ZnEcL/TAsx3KCkYqCySKpBe1B0KIqm0tAl8cx7qur66ufulLX1I7Y0EQqHinaVqaplmWKYKP"
    b"okjF4NlsRildXl42TVONaE+nU3g6xut5HsZYzVCoK1N7S1mWVatV1YKheKBarWZZFoah53nK"
    b"E1utlmEYQgjP8zRNsywjTqPRaNjptC3X8cuVZrvdH40azWZS5HGe5UXRPT8bjgaT8Xg0Gk7H"
    b"I0MzZrOZEKLRaBiGcXJysre3N51OF9M8alwTANQDJBaDJ4SQJ8ha2FLdmyIgFQXa7bYK7Zqm"
    b"qRnhfr8/GAyiKJrP55qmNRqNs7MzBb0gCKSUlNK1tTWlnhzHCYJge3tb+X+pVGq324r7VM6g"
    b"VphS6jiOikcA0G630zRVgQlj7Pt+tao2fePV1VUVyxBClmUapnH9xeu+77c7bb9cNi2bEu38"
    b"/DwMgrOzs0G/v7zUXl1ZNU0TI+nYDsbk/Pw8iqI0TZvN5vHx8U9+8hPHcVShZQEXdfzFuMCT"
    b"aFipVJ4dUlmMRT1pskFoPB4rvbO/v6/reqlUUnJRHfHRo0d3795V2dInn3xyfn5+cnKibnsR"
    b"UFRwYYwdHh7u7OxUq9UoigzDsG273W4rfacCU61WGw6H5XJZ7chVKhWM8dra2mAwaLfbnU7H"
    b"sqyiKJaXl1utlu/7g0HfcR3bsggis+lsZX19Np9RSj3bNhDaXl0rOU6eZUEYbj+3xRjTKN3d"
    b"fbyysqKWZ29v7/Dw0PO80WiktvsWpSv0zDz24kVqtdqz4ylPepifFk4VLIMgYIypyNhsNlUN"
    b"59GjR0dHR6VSqV6vq+1YSulwOGy3261WS5HiaDQCABVDms3m2tpaEATdblcRZ6lUiqJIsdjW"
    b"1pZyvaIoqtWqrusK0a1Wq9FoKHKsVCqNRkOxr+/7CKH19TVCyXgyqddqtUadFzwviul05rme"
    b"QahtmIBRtVbLWXb//v2XX355PB6vrKxOp9OTkxPLslZXV2/fvn12dqbcbfGQFPj5ocsFxIgK"
    b"QPDzY2QLga+uUkqZ5/nm5uZ8Pvd9X7Fvq9VyHOfZ2wiCYGlpyfd9Qsjx8bESrq1WixAyHA7z"
    b"PB8MBnmeD4dD9VsAmM1m7XZ7PB6vr6+bpmnbdqfTUS5frVbV4wmUWRUclGqp1+tHR0dra2tB"
    b"EJZ8H2OSpJlhWsE0rFZrgCBjBcJIUjyNAst1KKJLneUPP7hl2Y5lWdVqtV6v53muqGM6nSZJ"
    b"smDtReandrwUyp5gSHHqsy9lKcVziqFVCB8MBlevXg2CoFqtViqVXq+XZZkqEHqe98knn6g4"
    b"pUjH9/1araYEEcY4DMOVlZUoinRdPz4+NgwjDMNer1epVKbTqaJCZaM8z3Vdj+NYSRPHcZRX"
    b"Kk0zmUwwxlEUOY5zeHhommaSpo5jO47nOZ6lG4eHR2EcAUKU0uls5vn+Bx9+uNRqM8bqzcb+"
    b"4YFtWSqAFEWh7KV24590uhOiRIOy2sITn0DsueeeU5ZTllr0IinGKZVKi50Ly7IajcbLL79s"
    b"WdbZ2Vm9Xp/NZkmSdDqdjz76qFwur66ujsdjTdNGo5HKxpWORQgZhkEpnUwm5+fnhBClAzqd"
    b"zmLdVOeFWhtFiOqlpK8iFCWvDcOYz+e2bUspx+Nxq9P2PM+kZpHE8/k848wuuVlRGJqmU02d"
    b"KE8Lx3PjPPN9//GjB75XUrJjd3dX0bE6/oKIVKBT+aOiXfUJaTQaCoELTKn/wxgrfl3MHgZB"
    b"oGmaitkXLlxQK2Db9vHxseM4lmVFUTQejz3PU5SHMR4MBiqGqiMYhqFqjSpdN01TeZlpmkEQ"
    b"cM6jKJpOp0VRJEmiYm4YhowxFbIV7tQBsyxTjgyA8yyP5wFnnOqUCyERSCHSOInjmOUFJWQ0"
    b"mXilEiKYUurYFsH49PS0KIrZbKbAruS3EkAKXGrN1E6zcklCCGk0GiopWayw2q9XV7ao1SdJ"
    b"opg4TdPr16/neR6GYaVSUeO3lUrF9/3pdKqSYaUD0jR1XTfP8yzLer2egqGqPbiuqyJmEAR5"
    b"ni9g5ft+EASqJqNpmoqMS0tLKu9ROohSqpIhdT+z2dQ0DSF4kiWMc6prSZxQQvI8T9NUSBnF"
    b"kWkaR4cHnuemSSy5ME2zXq8fHx8XRaHKG8p1CCF5nluWpWxnWZbqZPiZ5125cmUxt28YRqPR"
    b"iOM4iiIVGtQlWpal63q1WnUcR22IBUFQqVT6/b66PWXiyWSiqgvqSR9qs1aRmm3b8/lcSXBF"
    b"nJZlqTRQ1S1M01Rqg1KqHg6iwqsSvVJKVVwLgmAhhbrdrlISUsp6va48oCgKx3Fms5nSAepP"
    b"FdMVgaqd43K5fHx8vLu7a5pmHMeGYSh+VHBRBS+EkCod/ywaNptNIUS5XK5Wq5TS0WikXENZ"
    b"SjmaZVlxHE+nU3WmZrNZrVaPj49VOqkKHUdHR57nTSaTNE3zPFdlFrUVUhTF/v5+EASmaary"
    b"ofLEJEkWD0ATQsznc1W9efz4saIqFXYnk4mq9qh0fTqdEkKerXwRQkajkRKAYRgqF1MBrlar"
    b"WZalkj5VLKjX651OZzAY7O/vA0Cv16vVaooKFBepjRvlUiqZWTyHijQajfX19aIoVJIMAMol"
    b"VVqknpg0nU4Nw1hdXVXj8OVyWS2Uunld14MgsG1boUOdWGVzioy73a6q5auWExXsFKyklGEY"
    b"KuJTGY9qN5xMJqrIo7IoFeMHg4G6QlURjKJInahWq5mmqaSTWl2lzlTT3nw+V+5v23a5XHYc"
    b"h1J6eHjY7/c557VabTweqxtRiZRyKVUsU6nozzTqzs7OeDwGAOU4KllTjwZwXTcMQ5V22Lat"
    b"bhVjvL6+7nme67pJkiwWwfd9RW2apqnTCyFUgqlkmqpzxXGsCoSqfq1yoF6vp+u6gqSqvVSr"
    b"1b29vVqt9ujRIwUZ5R0KeipmqZYxlWk6jqOYUSFauZ6iP8U+qo6odFySJOPxeFGzVA/yU6v4"
    b"rCJVt6acTFVKSKVSUX6nmGIREXRdV25i27YiQl3XDcNYWlq6cePGIteVUp6dnSlmUXZZ1DQU"
    b"JG3bZk8r2WEYLtghSRL1uC9lPuXyKpBPp1PFDOfn59VqNQgCdQPK5dXmJkJoMBj8f22dyXPi"
    b"VhfFNWAkhEBiFFMDjt0e4+rOwulKUtlkl002+Z9d2XWlk1TKTrttYzCTQExitMW3+LVe6NTn"
    b"RaqbuAFd3Xfuuefc92Tb9nq9dhyH1C6VStRKiunLywsYAhLl8/lCoeD7PjIGgLANDzpCXwQN"
    b"Sa7NZsMHiVNFFExDOTys5+XlhYPtkCwAYyxYwzCwNn777TdQ3DRNSZKSyWS5XOYjx+MxMhAf"
    b"kE6n+Vrr9Zq2ebFYoEzxVbrdLqIzfb/v+7e3t6QA92w4HFIouHIGXyEQ9AaVSoX+yTRNFgQS"
    b"ueM4ME8oTrFYRAqm9H8eqFXV5+dn3/e5E7sSja7rREZoVpvNRi0Wi0IMpOHgekA1FDgOMVsu"
    b"l77vdzqdX3/9FcKJ0kLuULlgkoiZ/AGyPhgMTNOEFrNIFUVB6vF9X9CCdrvtOA60i8k64kIz"
    b"CNzA1GCMtm0vl0vbtlkHnufBQtFagyBwHAeEJh8pLI+Pj09PT7CE9Xodj8dhDxRQcToW+chV"
    b"fNaXyuWyFA6GcIIRwLQNjxBkxXLHKD30iXCCdDpN7Scugr8xxsR7Qu2AGPQpDgzjxjCxEwTB"
    b"YrGgPvDpICbORSQSwSe3LKvb7RqGEY1Gs9ks6qBhGJ8+faLHIiiMJdCBcyPJrNFo1G63//rr"
    b"L/xQaguJAkIBVf9GR1VFECRJUl+9ehUEAfcKHoSEJFokZDAwy7IsbjUIiv4XiUTANWQvVEfe"
    b"Z7lcsloBEaIZi8V0XWe8iYVGaQMyCFYkEkFBlGUZvgJpCIKgVCp5nhePxz3PI8uE1UTd4BAb"
    b"cJYifnBwAAqbptlsNgEy0genTg619l31ih9A/DPP4gTcbXiwKdEhxcRQDasdjvfq1SucCNM0"
    b"U6mUJEnIhC8vL8PhEImVCUwwfrPZPD4+CiID2fN93/d9bCFqkOhgqdbYB3BdWZYZna5UKjga"
    b"3BXK4mw2A9RZudyJSCSSy+Wy2axhGLlcjroxmUwGgwEMi09nYlbEQg6PvxXKzOfD+4IAzV2t"
    b"VqtKeG6dAC+gB7oRjUaF+F0sFp+fn8vlsu/7pVKJegwisi/D87zZbBaJRMAp+kHwKBqN2rZN"
    b"qs9mM3gDtZk2O51ODwYD13WTyeRwOEQOoctFU/Y8jyuHWBcKhfF4TJ9I4kiSxNQnUqJlWZVK"
    b"JRaLDYdDyIeu6zc3N/P5HMkTzBFE4T+6HsFinbEe1VqtJlzo3dNOqYDkGvLIZrMZDodYOJeX"
    b"l5vNhiacJPI8r91uJ5NJ27Z7vV4QHlhL6GErcNFGowE802ACQJ7n4c7yhuIAZTwFnGHhfUJi"
    b"1ut1KpWiCMKt0um053mxWIyhDdyzyWQCL0ELQw5iIePgkonIWOJHeKC7iaZWq9V/eUT4Q+0U"
    b"fRw3Qdf1RCIxnU7j8fj79+/fvXvHOCA3J5lMplIpJit1Xedi4PHgApnseR60G46O8kPIQCtB"
    b"cBaLRb1eJ7N837csa7FY8MuJRILc/3zDVRVUHY1GjPXT4pim+fT01Ol0yBdFUVar1d3dHdY8"
    b"vFLXdapNJDwV+T/IJTJOlmW1VqsJRYKUY6WIcTcpPH0TiMXuPzg4aDabx8fHmM+KoqB4CIAD"
    b"FGhWBDOAxENfc7mcLMu8m9ipQDGh6u3t7fV6vUKhIMsy7k6xWJzP5/gd0Wg0FovBS6LRKFWF"
    b"1YfSLcvy3d2dZVnFYhHddTQa3d3dYe1UKhWKFV46mb4Nz74V6h7BEhqyymwMN4pluFsHISC8"
    b"TjQ5hliSpMvLSwwSuK8cjsPNZjNkqVgsRvu+XC4VRaFZm8/nUFO+32KxgMTJ4WABVRWnM5FI"
    b"tFotyBQqBZmu6zo3qd/v826yLNdqNQoLXudkMmE/xHw+Z9BD07TNZkNBazabT09PQO1256w1"
    b"UdOE0qDsnOOqIuO9hKeakhf8SzACcgCWQe6Xy2WlUsGAAPjpctBCWZWLxWK1WrmuGwQB5sJk"
    b"Mmm327hn4vdJNNQFposURaHNpNF5/fr19fV1KpVC7TFNk4/j4ESyidixpqrVqrhUSDJ8hfx1"
    b"Xff6+vrx8TEIgkwmw20AUgkKiw41RRRHkTfq/v6+FB4XLKJLFZPCA175MIiloiivX7++v78/"
    b"Pz8HU3nT6XTabDbBBdFkGIZBK4OJj+AZiURs2wbLOW4UwELwgk+Tv8/Pz/F4/OLiotfrGYZh"
    b"WRbyA5ioqqrjOOVyGfXx6OgIOxI2EI/HwSNEyslkcn9/32g0rq+v1+t1qVTi4xik4GLJD+Hx"
    b"cAkC3RVFUff398UKQg4mnAx9CPDjRQqK53nHx8eKohwdHSmKous6C01RFM/zRqMRRRcPjTmk"
    b"VCrFv5VC31vTNF5kzQrGzFBYu91erVb5fH42m3U6nWKxCGWlpFA3aPvpHCErONiNRsP3fVj0"
    b"crlMpVKbzabRaLTbbWQJaBf7cJjMISegAbyt6BZhJERN/eqrr+TwBH9RNUQmEzuAn71OXHy/"
    b"33ddl5UIxArODYJgf7HAE4nEer0m77BUUayg/oyHgFaLxSKbzWLcs4uoUChks1m4eK/XIyjU"
    b"+0wmw5wPmZXL5XzfZ+FXKpV4PO44DuCIV9Rut5Gk6RlZ1+QHCQVeswa56pedvSeKoqiHh4cs"
    b"MZFWUnjCPk4yHEdRlEKh0Gq1eF/WyJs3b9LpNMlPiJnwe3p6AuCBDLrFUqm0Wq2y2Szq5eHh"
    b"YSaTabVa+K/sQgDy6ZCQNHhPSjYzeTRbtMq4cPl8Xtf14XBIW7pkkQAACCNJREFUIti2rWna"
    b"3t4e6uPz8/OHDx/6/X42m221WuPxuFqtappGZnHJ4M8ufwbjgFfBGVWsMK52l1jJ4QHVTJHJ"
    b"stzr9Wq1GurS5eXlarXq9/tff/31Njy0Eo1lPp8zYkn/RdVDn2FQDUBZrVY3Nze0/pybfHNz"
    b"8/btWyosF1ksFpHrOp0OWhidFu23YRjVajWTyWBtUM01TePmocQye8UYi+u6kG16cngMBA2c"
    b"ETqf6E+DnbP0FUVRj46OpB2HWhAz+B7ojspuWZbneQcHB8PhcDQaXV5evn37FvrKtyTi9Ia7"
    b"vbHgAdwMdB7XdXFAUA7++eefQqEwm83Ozs5UVSUEsND7+3tWOu2qZVmWZeVyuVwul0gkqDmm"
    b"aTIJQNZDxIRUx0A/SrFt24RGSDGGYQRBAPyRaPwCq0rQriAI1OPjY7H61C8Na0LO54Eg3Fsa"
    b"WkmSGo3Gjz/+aFkWg4CUAqGgJ5NJGn1gDlUE5R6Ioaej5FM0j46OVFXl+lGTJ5MJAjf9VrFY"
    b"nEwmvEkmk8lkMqPRaDKZrNdr4judTm3bliQJFoIixCgZy61YLBJ6AFQQi90GebtztnIQPmtG"
    b"VVWVukbxovPiAoguRQGyC87xCwcHB4PB4PT0lA5DiEEQAk3Tut1uIpFIp9P9fp9mjZbb9326"
    b"MFEZuQDGub/99ttYLDYajYgvDTBpkkwm0+k0pME0TRDn4eGB1o8JL9d1gcjtdptIJBCwBoMB"
    b"XJqTrT9+/AippgMVfZiQaERlEzGSw1kQ9fDwEEijKBCml53navA6ZqQUjk64rvvDDz8MBoNy"
    b"uYwzTM7jOOzt7eXzeeYQX15e+v0+SA9f7/f7vV4vmUwyC6lp2tXVFYZgpVLpdDosltFoxPRa"
    b"EARsisTgUVWVm9fpdJANkM/W6zUrlM4xGo22220qEj/NZpNOazAYPD8/01ERCJRbeWfkXQll"
    b"K9EzSpKknp6eyrLMvArTqGL6TTQBcvjMCCkUpDOZzPv374vFYrlcRmslEAK5+v1+LpdD3np4"
    b"ePA8r9vtSuHeO6SCRqNh2zZfnQHyDx8+VKtVij1rdjqd0j9Cl6iSmIO4JHSOaNDJZJIVjfm4"
    b"Wq0qlQrTqovFAjkkkUikUilmX03TNAxD0zRwcxe7hbD1RbBOTk5Qbcgp4U6r4WNJgvDRKOCa"
    b"rus446VSSdf1Wq1G80iJ4X2WyyUMo9frNZvNer1umiZRQMB4fHxE9vrjjz8SicSnT5+goD//"
    b"/HMmk8FQYKKbBMTRApXhlo7jwO/j8TiTXPBV1GpMOSZ/GNskyplM5vb2FpyhSjI8QGVAlhGs"
    b"nTUkumhZltWzszPiF+w8ikGINvKXQ24EDp1fUZRut1upVAg3JRmBQZIkXNVsNus4DrnpeR5a"
    b"HdVqPB7jj2CsXlxcHB8fM+qWzWaZzEOr4VuRO4iLpmnSJyPV4tBg/eq6PhgMer1eKpUCyLm6"
    b"fr/fbre32+3Z2Znv+4eHh8PhEANNkiRu8zacuN1lBbsZp56enlL4IBpgHlqPCNZuMxmJRFar"
    b"FYpluVz++++/f/rpJ9Eesih0XZ9MJkA1jJmqj+UBJOOtQcdB6Pl8nk6nsdpVVUVWlyTp+vqa"
    b"eH38+BFDiDLKTAYpwwhcp9PhIimaOD1CL7Esy7bt33//PZFI3N/fHx8fM6uCOURZkEP7XlTD"
    b"XVIl//LLL/yFEo4PJkqmWK6KeJpMEPBrjuO8efPGcZx6vR6Px2m7ABEAmNCwUUAJn3qEY8hQ"
    b"xXg8brVaUOdYLOY4DoCNFSp01FgsRsf78PBAEKHXpVKpXC4bhtFsNiFlp6enqM+NRgPbAs2a"
    b"lGRIwjAMZGVRpgeDAdyYgXaCK1j78+7enYuLC1RNdeexKcRLrER+eH0vfFCNqqq6rufz+Vqt"
    b"BuHu9Xqr1co0TT4VBGEASpZlTdNAdFVVJ5OJ67oPDw/pdPr+/j6VSjmOg79bKpWorWAWky2d"
    b"Tmc6nQLJbIlhfnm5XE4mE3gDIe50OrSQpVIJ+Yg6zk4IgUSPj483NzeapjENu91uB4OB0FcE"
    b"SZLDJy58xqzT09Ng54F1Ii4EdbfHVsJJcfrYer3O1KzjOJIkMVfEbATfbLszqIWSqapqv99H"
    b"5zUM4+rqinkAWZbj8Xgmk2GYy3XdzWbz9PS0XC7n8zllFHFN1/XRaIQsQxZDwdGz6B+KxSL3"
    b"ibZ5PB7PZjMSNpvNTqdTz/PwgYIgoPFCO/lM01X1JXxIh1hSn3vB8/Pz/4TpXzwLx83F/5LD"
    b"kUlJklzX/f7777/55htZlukVEPagPMlkkqYHekny9no9sH84HLI6ttttoVCwbTuTySDLBEGQ"
    b"TqfZDEOBkySp1WrJslypVKLR6Lt376gS6DwvO89T4q5ATZj+SCaTpVKpUChsNhsYrOM4BwcH"
    b"V1dXZ2dnf/75J1QjCOfZuGqhU5Fo4v3/T7D4r3CGg/CpXOIPmqadn58fHR1ZliWm1TFfdxsU"
    b"dsNQkjqdDujALoy9vb12u12v129vbxkta7fbWKT5fJ7vHY/Hh8Mhc1hsHpJl+eTkpNlsdrtd"
    b"ODotFFwUvZS9ZAhk2Wx2sViMx2M01f39/XK5zMTdyckJHe52uwWtIuFGAQFEcvggI8yhLzJL"
    b"5JQUOrREnbJFjdA0DYGl1+t99913hUKhXq+vVivEP2GasoPFtm120VGMWq1WEASu6+ZyuYeH"
    b"h1gsxow3l5TNZg8PDxHIZVkGzvv9PtuQQatMJgNyw9GRD2VZxqdYLBaM21H4qEJcAsAHPGFc"
    b"c/6VGL8CKwRqb8On6kg7QrOqqv8DjxomFsSpzQwAAAAASUVORK5CYII="
)

# ----------------------------------------------------------------------
icons8_administrative_tools_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAAAXNSR0IArs4c6QAAAARnQU1B"
    b"AACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAXWSURBVGhD1ZllqC1VGIaPjV2YYNdV"
    b"FMQuFDHwly02Jooo6g8xMFDEThT7h3FtMLFFQcTEwBY7sTuw9XnG/XHXnTNr9szes8/lvPBw"
    b"zqy9Zvb6zqz11RnrWHfDvxX8BFvDpNA88A9UGSJXwKTQOuCCXyyupmkTcPzJ4moSaG9wwTcU"
    b"V9M0Pzj+I8zkwIzS6nAcLFxc5XUGuGDnlvUh+NlyxVVeG8BRMFdx1aHcLt+Bi/gEtoCc7gTn"
    b"bVdcTa97wM+2La7Ga1Y4Bf4C5z0MnRmTGvF57+ffcDbMDqkWgPfAOSs5UFK8rfNgZgcSLQtP"
    b"gJ//CV/3fu/EmNSIm2E2OBb+6I09D1NgU7gDfgPHv4dZoKydwc/FN3sqLAq7gfc4/j5sDCvD"
    b"p72xoYxxgWHEjZAubG14E/wstoE4fypsBFVy6xwKeq5w0b/3fspNoFMIpcbcDwM5iYPBB3wL"
    b"czpQ0txwJTjnAzgI5oCmWh6uBreRgXJfqNJe4Hc4bz4H2srFvwY+xPOQ0zLglhtUS8Fi//86"
    b"Ti7creYadAIDyy3kefBwb+7ABMs3phHPgNtyKB0PPuwjWNCBCdKO4Pf+DJ6VoeUh93D6UD3X"
    b"RGhxCPfr2etMK0B4pxUdaKAlQXd7OBwIW0JTZ3AO+F0PQKfpjIvwwe9Cv71qevEIeK68J8U8"
    b"61zol+bsCs43TnUqA5IPzrnIkMEyDPgBbofz4VJ4GuKzj0FHkpNR/1Vwbl061EpuERfwFdS9"
    b"DY3wi/X3J0JVJF4N4o9iJDfo5hRx7JriqqUsitaFfeBMuAv0Vj7wKshpfTBSe462caBGOg+j"
    b"v898qXddpUXA5xn5nwUNOgZMOD2nufvGboNcZWd0r9sKngnnnVRc9ZfJZgRb65ecLod0HSm/"
    b"wu4wTjHhBbgerCdMxWutR7H1PBNtErs9we/TM9VpXlgP9gczDEsBE07vLRdvhcKQttoJvM/s"
    b"t42iYjTgtdUe0LkhR4D36Z3aSgfivW2TwZEYcgB4ny62rdzn3lsu0PqpkSEWNWlN0E/6ee97"
    b"qrhqrlXA+4wpbWQleTpkDXGvhjFi+myjzZs89LkDb9phxPbAr+pAQ50Gfk9dn8sS4TBwjvme"
    b"DiVdo15tnLYCb/Ava6GT3iDGlpw8H84x2NV5uJCB8RfQ+DUdyOh1KK/DuHYv+IfQY9bKRM0K"
    b"bnu4CHzAg5DTQuAWcd51UJcc+taiQXGZAxkZt5zzJfhWNoOhygjTki/AAitXySkbFdFAMNhZ"
    b"opbrb7sovgnnvA0bgguuIspoA3XV5yk2MBop0mrbOHUyd3oZnBtYV4R3GhVmJBdCXy0B5j0u"
    b"qJ9HM3P1bRixUwfi1rN0jTTIPMszNSyPQrShrCprZfruRHOuNq5ZmWLEmVkDfM5nYI3TFVHb"
    b"XwBZWR3qXp1owTOMoiM/KrJB2YNuQeQkvdGwCkNs5FVtk0F5A2oNsaXpBEtct8iwCkMeL67q"
    b"ZdOhX0kcOgSyhlh7e8BFN1klA5KNs6Y9r6aG+EznPQflZneVag05GvxQ91nVV7JD8g04Rx4D"
    b"U/q6mqTKEANkutgwwj9gZeFUoVpDXJD7zwk2kk3ylCn3teC43AfvJNcGPONOlcqG6MUMojYp"
    b"bNGmRlh4NVWtIapsjPEherF6sv1AmV/pw43CLsJYYf1flvV8aoiGRU0SKU5bI1RfQ1RqTGBi"
    b"qVuuUkR2mxhlRfs13VqW0m+B46kRR0JdSpSqkSFKY0wabfWcDHVtIf+X4kOrsmW3UNkQZdJp"
    b"hPaNq0iJ/M/w0Ie9Sk1K0hPAh55VXE2vaC2lhqwFbs1ojYYRJqk6jyZqbUgT7QA+1G5HKreJ"
    b"46khdkd0DjoM49QgRqiRGBIlrC2bXRLCI6WGeI7Muxyz7vBnWyPUSAxxm/RL29OttTS8Ao4P"
    b"YoQaiSHK5PIWuLXEQ1A2RJlRuxUNsoNoZIbk1CbXaqMZZohlrklhV9gWmlBDPNx+4ai4GCZE"
    b"OgI79raduuaSsbGxKf8Badt0RMmhpAUAAAAASUVORK5CYII="
)

# ----------------------------------------------------------------------
icons8_play_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAAAXNSR0IArs4c6QAAAARnQU1B"
    b"AACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAFKSURBVGhD7dm/KsVxGMfxX4pBNjLJ"
    b"qpTNYDqDhUuQO1DcgMEVWIwGC5egcwVyATLLjAUpSf68H3zrk4iDzu/7PJ53veo426fw/Z3v"
    b"abIsy7KspbYx/vrSd5e4wPLLT46zIU9vupiEy3SIucYqBuCq90OKQ0zDTTrkRl6bO2xgCNWn"
    b"QzrYwaO8Z44xh6rTITP2Bs3jBDrmAVsYQZV9NMQaxibuoYNOsYjq+mxIaRZH0DFmD2Oopq+G"
    b"WINYxy10zDmqOUi/M6Q0hQPoGFPFQdrLEMsOyhVcQcfYQbqG1g7SXoeUJrAPHWNaO0h/OqS0"
    b"hDPomFYO0t8OsUaxCx1j+nqQ/sWQ0gLsnNExfTtIc4gU4lfL/R+7+3+/IQ5E948oIR4a3T/G"
    b"h/hg5f6jbpjLhzDXQcr1BZ0JcWXq/hI7xNcKYb7oybIsy/57TfMMeVT4gW4EYDcAAAAASUVO"
    b"RK5CYII="
)

# ----------------------------------------------------------------------
icons8_pause_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAAAXNSR0IArs4c6QAAAARnQU1B"
    b"AACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAB2SURBVGhD7dnBCcNADETRrSrFpI8U"
    b"k3pSWGzBuACTAQfzHuiyIME/7wIAfvfY5515zcNJs3Psz63LPPf5Zj7zcNLsHPtz6zJCQkib"
    b"kBDSJiSEtAkJIW1CQkibkBDSJiSEtAkJIW1CQkibkPibkNt8KwDADay1AZozwcm8F5lJAAAA"
    b"AElFTkSuQmCC"
)

# ----------------------------------------------------------------------
icons8_lock_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAAAXNSR0IArs4c6QAAAARnQU1B"
    b"AACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAGGSURBVGhD7ZXBKkVRFIZvMeAJJHkB"
    b"JSVlIgOKKIw8gkxkes0ljyAPYCJRUjIykJmRIVOlKDGgUPj+Oqu0w3G3e/Y5buurr07rnL32"
    b"+m93n1NzHKc0OrEPx3Esu+7Af8Mc7uEjvgeqtouzWFn0i59iOPx3nqDWVIppfMBw2Ce8zNR1"
    b"eP8ep7ASjOIz2nBvuIM6F+1o6FrnRX8tPWPPa+0Ilko33qANdYcTmMck6llbpx5dWBqbaMPo"
    b"IA/gbxnEzy+EDSyFXnxFG2QBG2URbb169WByltGGuMA2bBSdG70IrM8SJucAbYBVFSJZQ+uz"
    b"r0JqztEGmFEhEn0crY96JucWbYAhFSLRWuujt1dy9DGzAfpViERrrY96JseDBHiQGPTN2A58"
    b"QRvgKKvFqLXWRz3D+9q7aWyhbZZa7d00WjLIMdYL9hALD7KuQsGsoAf5CQ8SiQfJw4NE4kHy"
    b"8CCReJA8PEgkHiQPDxKJB8mjJYNc41nBXmHhQVLrQb5iGOdLUns7jvMnarUPpRqxAEGuZ3QA"
    b"AAAASUVORK5CYII="
)

# ----------------------------------------------------------------------
icons8_move_32 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAAARnQU1B"
    b"AACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAADiSURBVFhH7ZUBDsIgEAT5hH/U6HP9"
    b"T+1GNtlcSuEKHIlxkoukhduxVkh/OrnlWgKC37nCJRi+5QqVsOGhEhpun0CIxGsvDaKAimHO"
    b"VB578VtSAOAa7oWiAkuYKoBHev8Oi7QIoAd/smb0pXriwkWwFj1c/w4Ndy08wN1rZDhp7qkT"
    b"a1XiaK6tosRyAaASpxMduHuOlLjcSxee7e24jyphzw4XWFDb22sCQM+O4bQITGWJgO7tKoBr"
    b"tbOjG7u3UwBjvrQ9Z0cVDeKnjik2FZXQCgknViI0nFBiSThB8LLwXyClD9l3kJtafbLiAAAA"
    b"AElFTkSuQmCC"
)

icons8_move_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAB"
    b"zUlEQVRoge2Z7U7CMBSGnxhN9I8OZEPh/u8AE2OiIVFQgciHIsLN4I+2aZ0BaffRzfRJmmwj"
    b"63lfoO1pDwQCtSWSrdZEwCvwBlx61uJMBIyArWxTamimAYzRJkwzLY+6rGgBM4TwL7QJdT2j"
    b"BmZiYI4W3kEbaQMf8voTuPKk8SDU32mJFqqMIJ8t5f2odHUWvAATIDGemUaQn02A5xJ15ULa"
    b"SCEcFR2gLIKRqhGMVI1/Y+S4hBhPlDD9HkIMPAI9D7F7iAwgztpRC507DbN25sBQxl6QIdGM"
    b"EKmESgCvc5FmRwy8Sw1zHMxE6ARwjR8TigSdNc+w2JxdoHd2a0Qq7ps2OmueAs2/XkhvT22a"
    b"y2Rw4xhrTOpAI72OnABnDoIAzkt6B+AUoXUvmQdYAThPPM4DrAAyTzwJlgOsAMyJZ0OGiaeD"
    b"+Ba2QD8PZZb0ycGEoov4ZQZZO3JgIGN3PcT+xR1w61tEHoTDBxuCkaoRjFSNYGQHPeABUejZ"
    b"RQO4p+Jri9rfT9C5mbmONNFZ7KJ0dRaY9Q9VZlNGzHLchoqkHfvo8LPMtk1dq0pWLTDLbGar"
    b"lQlFgt5pboEVNTShSBCDeoXfI6VciMnhyDMQ8MQ3mEmjvi1225cAAAAASUVORK5CYII="
)

# ----------------------------------------------------------------------
icons8_route_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAAAXNSR0IArs4c6QAAAARnQU1B"
    b"AACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAHQSURBVGhD7dZJTgMxFIThHIIlK2Zu"
    b"wIYdO7ZwAeZZnDV7FszcATFUCT/JMk7Hr+12/KT+pRJR6LjzKSCYjI3Z7cjNdAR8uZnFCOLH"
    b"zSQmRJjEhIgPN1OYGGLbzQxmFkIygZmHkJrGpCKkJjFahNQUpi9CagKTi5AWiimFkPjad6wq"
    b"pjRCqoophTh0X8OqYEp+Eo/Y/d/Dfw2KKYlghPCcqpjSCCYQrgpGg1jGVhL3ismZ3KAY7Scx"
    b"xeTaPhsEo0WwXMgntobF6oXpg2A5ECIOsK7UmBKQfT7Rkf/LnoJgW1j2p8IDND9aqZBBERIv"
    b"/MbkxTyIB85KC9Eg3jA5m+8pGSFpMBrIA5aC2MSyEdIx5mN4MG8QpoHsuq9dxRB8L1mlYDSQ"
    b"efFs/49mEYR0gvkY3sjH7GB7bkt8omcbWIjgvYt2ioUY3rhUMQTvOUhDYXjGC1YFIZ1hPoZv"
    b"IAezjoUI3qNK51iI4RvSFkPw7KqFmGdMg+G1fM1CEdIFFmJm/Rfrx2tCBM9aaJeYBhND8Iwm"
    b"imFWsTA+1yxCusK6MDEEX9Nk15iPecII4PjYR/DapothzCGkG8zH+Ah+z1S3mI/hYz5nMsGY"
    b"Rkh3bmNj9ppMfgF/kbj+SZ89mgAAAABJRU5ErkJggg=="
)

icons8_resize_horizontal_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAAAXNSR0IArs4c6QAAAARnQU1B"
    b"AACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAECSURBVGhD7dhZDoJAEIRhzuNyKJcH"
    b"vYnn8VjewaWbUMkEDRGmu2lI/UmFt2G+RF9oGGOMMcbaNt3TMo8zB7vInt3TKo8zB9MXvWTv"
    b"7nmU1XaWlWe6Y0qE7iHbymrbyfQsnOuK8UKgEIw3ArliohDIBRONQKaYuRDIBPMLoQdHV4XJ"
    b"gkCTMNkQaBQmKwL9hbnKSoTuLrslm96pvKPeWe/edpD1EUua3l0N64Foq/hpoT5mCX/2LwTK"
    b"ihmFQNkwkxAoC6YKgebGmCDQXJi9zAyBojEuCBSFcUUgb0wIAnlhQhGoxOjT4gPdSVae6Y5A"
    b"+iLrz5s4MwyBVvERmzHGGGP5apoPcwpl40zo9wQAAAAASUVORK5CYII="
)

icons8_resize_vertical_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAAAXNSR0IArs4c6QAAAARnQU1B"
    b"AACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAFSSURBVGhD7doxTsNAEIVhi3NwmECB"
    b"aJLj5VQUUHOOFFTJPMlPWq1md8aRbM+Y/aUnnBRxvm4NTKNR3j7mpe4i+5uH65QRcZ+XElMj"
    b"UmLOMg3BpcBYCC40pkbcZF/Fa1zjPb4OidEQb7Jr8R6u8V5YTAuBaggKidEQJxnTICgUxkKg"
    b"FgSFwHgQqAdBu2K8CGRB0C4YHP68COSBIA3zKVutV9mvzINAXggqMbgH7rVquMGPzEKgJRAE"
    b"zLdsdQR7mX9aLYUg72dv2jOQkA1ItAYkWgMSrQGJVnjIIY4oPDTigGe1FPIuw2dvcvItj/EW"
    b"ZgkEiM2O8dqDVQ/jhZTPItjqD1ao9+ufOg9EQ+z63K5hLMiuCObB9CAhEMzCtCChEKyH0SAh"
    b"EayFqSGhEUzDpPuzAqsxrYVGMAuTAsHwRTVMKgSrMSkRjJjUCHaIf+EY/dOm6QETlEg8SIvm"
    b"sQAAAABJRU5ErkJggg=="
)

icons8_save_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAB"
    b"XElEQVRoge2YS1ICMRBAn5aFx9E1eD0/HEV3bLwAehOHjZ5BXBBKoDLm051Jl/SrSg1Uejp5"
    b"hGSgwXGcUmbAEtgA207tOcxDxFNHgcO2ksoMIdF8pH8/UAv2ub9QkElNdAqRG+AzvH4FriXJ"
    b"avtTvHP8FVqP5L5FuDKtRWL7YSy3aGWmEonliuWulrEmApUyFkXgeM+8lA5U01+Sv0QEdjJb"
    b"4Lt0oJr+kvylIqMxl4IJSVF9FvUQeTt5v45GKWDhyV4cU7Mim3BdVNz7F3fhOmglTH0qjwcx"
    b"Ldq9cH7ZgbMgM6Ar8BEkUr+p1ER6Y+74VcVFrHHWIi2rLAO7E1FcQYH0qTVFleVBML/swFSV"
    b"RcKC35UZQ02k9XOmavyz3uwmcRFruIg1XMQaLmKNHJHef32zxv83K3KVEXPRfBYK48dWpFUB"
    b"ToOiIl7rApxGSxXxgHYFOI2WW8RzHOeEH/58jcLJRDukAAAAAElFTkSuQmCC"
)

icons8_plus_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAD"
    b"yElEQVRoge3az29VRRQH8E+18h4Bhb5aYCnxJ2gqe4I/FmoRF2iiiYo7DG74EXSr/g8mTfxH"
    b"DBGjCKKxiigbawHdqCSaYOOvCkHzWMxM5tb0te++N30tCd/k5iR3Zs6PO3POnDlzuYnVhaGC"
    b"vFp4BDuxHXdjE9bF9r/xC37AtziNU5gtqEPPaOIVHMd/aNd8/sX72IfGgHUHa/E6LlWUuoKP"
    b"8Cb2YhtGcFt8RuK7vXgLJ+KYNP5nHBU+zkCwB99XFPgS+7GhB14b8SrOVPhdxO4imnZAE+9W"
    b"BH6FJwvyn8DXFf6TlmF2tgiKtwWnPYhbSwuJPA9jTp7tzaWYbxWmu41pPFSK8SIYx0yUeSHq"
    b"0BfGKgy/wJ39MqyBESFEtwWf3NIro6a8nD6T94NBYh0+l5dZTz6THHta2OxWCqPyqpisO3iP"
    b"7NiD8ImlMC4HgIluB62V94mDBZRI4bRfHJGdv6sl9oa8T5QIsaUMGcY3kdeRpTo3hFShjScK"
    b"CKecIfB05HXJErOyT44QpVDSkCE5kr60WMcPYqf9hQRT1hA4EPkd69ShJaTVV/SWAHZCaUNG"
    b"cBXXVPS8pdLhUcG5P8XvBQWXxqywSQ4LBznMN2RnpB8PTqeecSLSXelF1ZBtkZ4bmDq9I+n4"
    b"QHpRNeTeSC8MTJ3ecT7S+xZqvCw4Zem8qrSzE7LwNn5dqPFqbFzTBaO6RYa6z1JoyHUCzF9a"
    b"NzSqhvwV6fouxg3VePoZ0wl3RPrHQoZcjrTYGXkZsSnS39KLqiEpWi0YCVYZ7o80Ra95hkxH"
    b"+vDA1Okd45F+l15UDTkd6WOD0qYPPB7pqYUaR+SkcWNBoaX3kZacNCannzcjs/hQiNHPFxRc"
    b"Gi8Ie91xlaj1f7wsfL0zBQWXPlidjfxeXKxjAz/Fjk8VEl7SkGcirx91cQ1xNHY+a/UVH85F"
    b"Xoe6GdCUa72HCyhQypD0gWfUuBTaHQfNyTF7JbED/wg61b7KmJS/wGhZvWphTMg62ninFwZN"
    b"oSzUFs7IK1HEXo+pqMOUPu4Zx4Q0IF0rjJXQrku0hEJIuo7rO5ndKk/tjMHkYjsqMs/jrlKM"
    b"N8vLbE6ovQ6XYl7BsBCdkmNPySl7MTTlANAWCsqlbl+HhKuMtE8kx17Wu/cJedpT1f6AkHTW"
    b"RQuvyWlHWkolb4sXRVNYXimdaQsZ6Um8jWfxoBC218RnVLg0ei72OSkXPFLaccgK/QHREKri"
    b"x4QjQN1qyTW8JySAfRlQ8qeaDUItdpdQtbxHCNe3x/Y/hTrURSGkfyLMSsdU/CZuZFwHvZQq"
    b"HNfefn4AAAAASUVORK5CYII="
)

icons8_trash_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAAAXNSR0IArs4c6QAAAARnQU1B"
    b"AACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAFwSURBVGhD7ZmtSgVRFIVHBDEIahMU"
    b"X0AFg8EgWHwEQRCsPoAWq8Fg1SCCVYuCJvEHk8VkEGwWX8AsFl0L9oaDHPHOZZ87w2V98JXF"
    b"MPssmDn3cqYSQggBpuEBvIH3Ge/gMZyFrWUSfsDvDvyE87CV7MHcov/yDLaSS+iLPIWbGQ+h"
    b"X/MMe8oAHO/AW+iL3Lbst2vQr3m17D8HYQij0Ic34RwMQUWCDCvi78gu9JufWxZtbkbYO+Ls"
    b"QB/CXakEvZihInVotMgYXDGXGCR4TocZGAvQ8wkGRqNFuHjP3xkkeE75h9J5hJ6vMzBUpA4q"
    b"YqpINCpiqkg0KmKqSDQqYqpINCpitr7IIuSZL31hkOA5nWJgXEPPVxkYjRaJREXq0DdFeDDt"
    b"Qx4YFOAE+gye3BdhGfoQegRznw66dR9+Qb//BiwCj06fYFqmlG8wPT4Kh1sot9jc8Cj5WzQD"
    b"izME+ShcwNwHz269gltwBAohRF9SVT/YcCJDemJ9EwAAAABJRU5ErkJggg=="
)

icons8_manager_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAD"
    b"60lEQVRoge3ZXYhVVRQH8N+MqZWplRA1RoaZ9IWFBUX2RfSBD4VFEdWLwWCYZS9F9RAGRQV9"
    b"GSRU0EtBgVFUmMQYvuijEVlWMAZJmYTgV1oONjM9rDvMvqdzzz3ee+begvnDgnPP3mvv///s"
    b"vddee18mMYn/HfrxPi7tNpF2MAt/YBQfdplLacxEX+15Dh7DoBAxZhtxN3pr9c5HT2dpFmMm"
    b"duJPfISD6gVk7Qdsrj2/0QW+DdEnRBSRb2SbqiRyQpv+v+EL3JG8G8UGDGAf5uM+XJjxfafN"
    b"vivFHPXTaS+uy6k3BWvUj8jHHeJYCo8bJzYiX0SKdZn6504kubKYpT46fZYpn4tbMT15dzqO"
    b"Jj6v63L06sch9VPl4aR8Lg7U3n+e8d2S8duJBe0S6m1eJRc3itCb4kDyfAlm156XZOrtz/w+"
    b"r1a/K1gkduz0yz6dlE8XI3EAqzO+OxKf/XgRp0ww36bYaJzU9yI6FWGxevHLc+pcgF14QozW"
    b"fPExdmFhFaTzcFeG2JqCuifjq6TuQczIqXdnps3UbqqKeBZTRNqRdrZORKcUi9WLGMVzOe0t"
    b"wG6Nhfwi8rQJwVjulNpRbMWn+K4BqZVJG1dhLX4tEDFmv+MtXFmliIUlOm5kXyftrM0p3yim"
    b"0s0iDcqWv1qlkB6RxQ7gHpF2jDQgfkhMp5U1EcuSdqbhp6TudkxNyqeqj3a7cVKVQvIwT+zY"
    b"aYhdLn9hp9iW+LycU/5aUr6tIq5N0SN27FGxT5RB+sU/ySnfoAtCiAi0TLnNrl/9lBzBilpZ"
    b"j5iOafnf8vegrmOVmILZdbWvZum7EbFGVrXS0RQsxXvYgyExFZ7BWW0IyOJBDGsc6YbxQCsN"
    b"XybC3J6CxoeEwCvaUZBgdUFfTx5PQ3PFgWl7QYONbItIW9o5Ql9da2tA5FtPic11FNeUbeR5"
    b"sZBa3eTG7GfxMU5tUcwS9eF6hn8fBwqxvgIRqf2Fd3Fxi4JaRtVC0kizCbfp0NF2ooSktkNE"
    b"pxOPk1uPONDdUsa3E0LGbBBnlhAwG4+oPy4MahL2OylkFC8UcFmEN41fhhf6tnvT2C5Oy/ye"
    b"Jk6ID+HaJr7Zw1sdOjkix4yH1LPxrOKNN+tbuKd0Ssh+kerfL27xjx2H77e4oUhEJ4W0Ynvx"
    b"qAbLoewaOYgPxDmgD7erLrdqhiN4BS/hcFmn7IgMinwnL9W4XFwCHDYxIzBc4zOvLPk8IVvF"
    b"X2XNLtyIy+wV+KZCEV+KzLtl3IuL2vC/XkzBoRJkGy3kpW30XznOEFMyvRlpeSH/F9Ar7qbW"
    b"yw+xR8TlxKxuEWwF54h7rR/FHdfb4hA3iUlMYhLl8Q8zzJ/A80nLpwAAAABJRU5ErkJggg=="
)

icons8_center_of_gravity_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAAAXNSR0IArs4c6QAAAARnQU1B"
    b"AACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAKRSURBVGhD7ZpLbtUwFIavQCp7AKmw"
    b"gjKAYWnZC6LlsQHGjJjx6GOIugr6WEQLzHirSygSApUB/F97j3SUJre2414nt/mlTzdNcmyf"
    b"xD4+djoaNKifei6+jeG4t9oU/8Zw3FsNjnRJV8WWMEc45lznRSPvizfivfgjzAmDc1zjnmXR"
    b"Kceuicfih6g2/Dy+ixUxJ4qKp/pV1DUyhi9iSRTRdXEkfIOOxTvxSNwRb4Vd45hzXNsW3Ott"
    b"KYsyi4g38kv8Fa/FvPCaFLVuCsYKtpRBWUVFl1g4PTyjkPCL7dS71Y3xb6hCHGlSbF3B4tX/"
    b"HP+GKtUR6mDMLJ78lVGEWItO9Od7IkQpjlA2dWDzWWQNzUQaaxDRpmlMVJXiyG1BADC7VZFF"
    b"zL5MXFYw0SlUKY6gdWF2LAGuiNYi7bBCeVLVEDtJqY5Qh38rWUIzsd4KZCKLUaojaEeY7StO"
    b"tNVHYQXG9tc2jjwRZkui2UqMD5/FkmLEqI0j1GW2v0VUpvxMvHD4QQcMdH/9PPaF2XJcd08T"
    b"1OXrpi3+Om1t1KHwxl2GtjZqZhyZma5VVcnBfleYbfRgr9MHYQWSqsSojSNZwy8qNSHuCbN9"
    b"yYm2KpGisHr0KUqWhVc1aVwToUp1ZEOYHcuHLEkjIjWxgnlSpNohSnGkmsY/FNnE4oZFDgX3"
    b"emGFWHay/Oz1Utc0zc2Hqe9xtd0OYkwU22U00QXozwxOohlh02uSI7cE0QlbysiyCkxR3ZYp"
    b"jdoVbGqTYlS3TDn3VHCPj0xQdMuULsEGtG9QCp9EaCS8MBEe+TTgJ81QmOweiOKfFbzIAOjn"
    b"pN8HoulDD+k8uRNvINuMfZHCsV5+eqtTSPjthQZHuqaZ+ReOQZdUo9F/xyvWUiCu12cAAAAA"
    b"SUVORK5CYII="
)

icons8_delete_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAB"
    b"bklEQVRoge2ZsW7CMBCGv3aAEdSRvEkbpLIUHh2G9l0oZaYDtkBRCPH5bJ8if5I3uD8f+BzL"
    b"hkqlUpkqc2ALNBmyGmAHzLQLL4EDcAGOQKsdcEfrMi4uc6lVeMFNwo8/4FMr4I4P4LeT9QO8"
    b"xRbuk0gl0yehIjPnsYQfJ3SmWetqDWUdEPbM7klhLZkxEn5sJQENt6YbI7MWZKwDJI7ASiIC"
    b"8M7jedvXM5uA2kM9kaQfQ2TOI2WyS6SQKSahKVNcQkPGjESMjDkJT8iyeQr8rGQZjyLkVzb3"
    b"T3TRkikq4YmVMSHhkcqYkvCEyqhKvGoVEvDihimkU2vs3iwLsc1uQkZr+S0qo/1CLCIziS2K"
    b"ZAMY8p0zGd4tMbtYMztgjQcpLqP5AMVkUgRnl0kZmE1mMgd0Fo9MvyQB1g6x90Rc/CxcgRzL"
    b"49DpzDdKdyRdmVQvrD4ZFQnPJK7ePDOu9xPio/0AVlwbW/0ytFKpVGzwD150jA21lxWtAAAA"
    b"AElFTkSuQmCC"
)

icons8_goal_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAF"
    b"vElEQVRoge2a329URRTHP7ttY+VXy4PUmhCNNj4QoCXRBLUSrZBY22CKMaGAkb+gShA1URIF"
    b"bE1DouEPsGhgK30ioomJTXyAqqE8+SNqVaS/7LZoKNQHpNr6cO5lz5yd3Xv3R996kknm3u/M"
    b"mfneOefMmdmFZVmWJZFEmfUlgU3ARuBB4G5gVYD9DUwDI8D3wLfAQpnHL0kqgXagH/gTWIxZ"
    b"/gLOADuBqqWa3EvALPA5UBu86wcuA1tN200FEvCVSeAAsLLcRK6pQS4GZBaC5+seMltMn3lg"
    b"HBgGPgPOAoOIWc3nITQOPF9OIp+YAS6a5+vAI6ZPK3ACMZU1eXTfAWwDjiEr7CM0EKEjttR6"
    b"Jm+Lj0yhkkA+wJBH/wjQUKJ+IB6Zq8C6cgwGdAJpoz8NNJWiNEXGJ6LKYdUvCbQA3cB54Dck"
    b"7N5CQu/XwHHgcaDCM24d4kuWTNErk8t2faXfEInbbxp4Fag2Y1cCfabtCEX6zFbEB+JMaMD0"
    b"jbuSYRkDdhkdCQ+Zj4shAuLIcchYIl3AFHAKeA14EdgPvAF8gKyE1bEAHMXNNCrJNrPnlpLM"
    b"j2Q2zThSgfjRBY+uFGKeodThBoAxYEUpZK5GkBkukEwou4E5o+uoabPH4C/HVV6JpB1a1iHR"
    b"KYWY0gCyElFkksDTwDNIIpkkWzYjX1qbWYfCE8BXCp8gZm7WjuROWyLa1QaTjyLTRSYA/AH0"
    b"AGs9ZPTKjOJGszYzTnscIv1B42vI1yw3mTD0Nps2nUbPKwpLAFcUlooikcTNZE8YzHd+KZbM"
    b"TQ8ZnaqkcU2xR2FX8ZvpbWk0E9qpsBYyNtxVJjJp02a70fGYwp4w2OZ8RPaqhvO4u2m3wqY8"
    b"feOSOWTadCusAphRWK/CqoF/FbY3H5EjquGYwc4r7FSO/nHJnFP4JK7JnlTYkOn3q8Le1oC1"
    b"s7tUfcZg96j6d6quk79ZYAdwSb17CPgCqFHv3jN6N6jnX1T9ATOH8RxzzSKyWtUtkTpVn1b1"
    b"7bg+k4vM6+p52Oher+rabO1K3lB1J4nM5/m3zLPehBKm/j7RZCrzjFWyWOVzqr7aYLNkDlH1"
    b"6v0EGTKQCdmzyGodQhz1HdXnYaNbm4w24VnTTq/CDfKIdvYRg+k0oU+9TyI7dq7Q7JNPye3s"
    b"Hyrsgumnnf2tfAPsUw3nkYuCUI4rbBrXyfVmtYCsQi55Ezeq6ZUqJPzuyUekyQyyTWHNBntK"
    b"YWvJPmecQzbRVUFpwV2JcD/S0WyHwR9V2JMGs4mtI0nkBjBsfExhFWaydtmbkbRjMWa5aSZq"
    b"s9wp3GD0rsJmiHHde0Z1uGw62F15t4eMvQnxlSnc9APcrGIROKiwJG7SeDqKBEh+pRW2Kqwa"
    b"SbFDbI7snKcWSTsmPQQmEZ+oMX0akduWsN3vuP7ZbvS0xSFSZSZh04QO3MRvzEMGZCU3IB+i"
    b"Naj7zKERCb86WDxr9Hyj8HEK2JMO4H6BToMfMficp02UJBBz0ivhC6v7DB4nvN+WlbhfKY2b"
    b"oiSQw401nSEkmvku30KpQKKTdmxt+3rV6nEDzChwZyFEQG7F9SCDuEuaQFbGd481g2yah5Gr"
    b"oP1B/ST+i4wFJJvVJKqAL007fZYvSAaMoj6y7bwDNwAUWq7g+gTBGB+ZdpHH23xSg6Qqlox1"
    b"tmrkjB0n9OoQfBA3OoGshCXxE9m5X8HS4JngIK7PhJJE9odexF/SwD9BSQfveoM2vsy7nmxz"
    b"mgLuL5VEKE0eMmki8p0CJAG8QHaaM0XE2bwYaSDbzBaR6NNGcb8QJ5HNTu8T2pzKthJW1iC3"
    b"4rmcthu57bA/FWipRhLAHnIHiRQF+kSxv7PvQg5S63Pg/yHERpENDyQDvhe4j9z7zBjyi/LZ"
    b"IudVlKxALpQnKD706rSjiyI2u3JK+IeBFNG39nbTPI34V8nn+aX4C8dG/H/hmEOi0s/AD8iV"
    b"0mKZx1+WZSm3/A9x0g4/FKsS0gAAAABJRU5ErkJggg=="
)

icons8_file_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAB"
    b"R0lEQVRoge3asU7CQBjA8b/GTiZOjq2Y6DsQnsVBjAuPwOAD6FM4uTj5BCjREN6C0Jm1mwaG"
    b"c7gO9E76nfcN3z9pQqFc75emoWkBy0rSUeR2BXAPDIFTgf1ugEegFhgrugL4ArbCSw1c/aOD"
    b"SQKEOOY4YpuhxI681t7rCnhHABMDkTgn/KbAi7deAR/AdZ9BYyDS/QC3tDEl7sgcjMkBgQSY"
    b"XBAQxuSEgCAmNwSEMBogIIDRAgGHGQOv3nslMAMuQl/OAbns+OwbuKGNqXC/PZ2d9JvTQT3g"
    b"LlZXHdu84a4oBr/r56FBc0DOgCfpQTWdI70yiLYMoi2DaMsg2jKItgyiLYNoyyDaMoi2DKIt"
    b"g2jLINqKgTTJZxEuOIcYyFJgIn1bSAxSAJ+ke9YeWuZE3KP+y1847oAR8o+r99XgjsQz7nGD"
    b"ZeVoB0LBdk/cOVz+AAAAAElFTkSuQmCC"
)

icons8_file_20 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAABmJLR0QA/wD/AP+gvaeTAAAA"
    b"qElEQVQ4je3VMQ4BQRSA4Y+o6NxBsfXWWyhU7uFOtA6gYhOtwhEUSoWKQkKt2Y2xwSw68SeT"
    b"vJc3+eclLzPTcKONRJwtTs+KrSBOMMXqhSxBBwMcYyenGEf2jDDDGt1Yh3XJscMCQxy+FZZS"
    b"mFelnwizIN5jib5iUM03ZSv3Q8txRu/TDjfFCknD5N0Oo/yFf+FPCqtXLxN/E6tkmJRJIyjU"
    b"/QIescEFrkM5GgOS//FxAAAAAElFTkSuQmCC"
)

icons8_vector_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAB"
    b"yklEQVRoge2YS0oDQRCGv4TgCURBAxp3egdd6BkiIngCEQSXwYXiYiKeQpc+Alm5EK/gKYwS"
    b"Nz52URMXXWPCMEPPo2cSQn3QTDJ0/39Vd9e8QFEURVHSU3KsNxiXf9mV0Lip5KRrm+mkK2el"
    b"DMwATaADvAHn5JegCyrABSbWZ8DD5ICHmaHR5qU08ce76hdGk5B4S5isFlKKRlH01upMTbGX"
    b"gauQ8x5mVm1tGWg7iKMNLMX0bIaMvwRTKB5mi3WlY5xirwNfmG3yCZyQvEZOZexAtOoxxlYw"
    b"F6QugWJPwzHQlwBugNlAgDZG+80Bd/K/L9qF0BDTH2A/IsC4bZQD4FfON3KK/Z9tMfqW30Gy"
    b"JAKwg5mgQYS+E2rAu5gc5mUCHInHB7CSh0GLYU3kjV8zLdfCGwxnadG1eAhVhlfEdZfCtyJ6"
    b"5lLUgv/odO1KcB5T3D2KWQ2fqnj2MJfozOxhZubBhVhCHsV719YxzrPWphzvs0SUEt9zy9Yx"
    b"TiJrcnxKHU56fM9VF2KvmOWtuRBLyIp4v9g6Bt8bxvbxIKv/1LyPRD2uF/7xIKv/1KyIJjJp"
    b"aCKThiYyaUTdR/K+T9hI7D81K6IoiqIoCvAH9xeE5oCkha8AAAAASUVORK5CYII="
)

icons8_vector_20 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAABmJLR0QA/wD/AP+gvaeTAAAB"
    b"JElEQVQ4je3SvUpDQRCG4ScmNooK/tQBCzsbTWOhtSAiURCsLIR4D2qrhZdgITbiNVgrCBIr"
    b"i4AIxkYQgiEIaQSxcENO1kMSsBNfOLDz7Tezs7OHfyKKKEdfsVtCFmvYxA0+o/0l3GEXJ0Eb"
    b"DlqSQRxgLIMGRvGA98g4iaNEsRL2UIt8I5hBI4djFLCDt2CYxhnqKbeqo4ltPAVtHKe4TfHL"
    b"4x5zoaOq9vyqQZsPnnxagZjrkNCLQvB2kI3iZUxoz6wbL1jABx5b4kBkWsV5H8VaXGAlrcN1"
    b"LGILr5j189eIKfme4UboMo9KJmyWdV5zX++BP+MwOqDQCsqROY7TSM2JZ/hrcol1KbGe6iN3"
    b"KspB+1FqGEroV3o/SjOKL1Hpo5G/xhdkBjoJ6swePgAAAABJRU5ErkJggg=="
)

icons8_system_task_20 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAABmJLR0QA/wD/AP+gvaeTAAAB"
    b"TElEQVQ4ja3UzStEURjH8c9goWyxY1jITkrs8AewoPgLSLKztLJR/gEpxcbWwsbWhrLwlh3K"
    b"S40lKYlmIxbnjJm57ryU+dXt3OeeX9/znOc852bQiS6N0VMG1zhqEHCsCR9YRf4foHxkfLTE"
    b"DxN4x26KeQD3ceFKmo4MBWAzcrhIMW9iXfWyDEWGpiomyKIPwzV8v6oFnI3ZNQw4hR101OFF"
    b"sYbQja2SuBlveMWtsPUnrKEtwXkWzqAM+IL9hDEXxzOMYBkPOEz4RtMy/JR+ynCKDdxhMWV+"
    b"qPBSV11wiW8s1DIWMvxCb+lKKZpDT3yS6sYjZHCOSaygtb6E/ygvtNeBCPyPloRDg/OWas46"
    b"dSLUF2HL2xisYG6P40uFOKmrTIWJcfQr9tdxHEvjGyk/jDRgFntC5tU0jxnF5kd5YxfULrRQ"
    b"rZ7LCne8DPgDBhc9y356EnYAAAAASUVORK5CYII="
)

icons8_laser_beam_20 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAABmJLR0QA/wD/AP+gvaeTAAAB"
    b"VklEQVQ4jd3TO0udQRSF4UeDCoJi4KhJEy8g2EQLQRtLCzsxfboo2NmIlaXgHxCTJm2wE0UQ"
    b"QSy0ECxELCLGpEolaiEkKHgrvi0eD4PfUaxcsGBm9ux3LnuG8rQZzlVlmcCy9XqBHWh/KWA9"
    b"NjDzVOAbFBLjU2jGbN7KX/CpqD+Cf6hz/2zqcIH5PBis4Qbr6MaHABaKgAX8Rwua5FxZFcZx"
    b"ikt8jWOVAmcjdomxcnZawFwknCeA5xH7hobS5AoMoTMB7sJH9OBnjHViB3vYTeTsw6Hs7lJe"
    b"lFX0KtyEpUfm/4JqvC1xG77jGO8wGH6Pk4i1JvKqE7vWhyNcYxt/ZMUaj/Z2xI4wKnuvj6of"
    b"C+jFKs5wED7DSiy6FcfciZxcDUXCpPsqT8bYoKygn/EXv/NgNbJiHUb7DliDHxgomluLxjzg"
    b"ROxkOPrL4Wdr2sP/2iDxiFO6BclXXCxkXMUWAAAAAElFTkSuQmCC"
)

icons8_direction_20 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAABmJLR0QA/wD/AP+gvaeTAAAA"
    b"yUlEQVQ4jc3UQUqCURDA8V/5RVAtwqBw0TmkGyhoeA33LTtHuGihtIs2FXoCpWu4EFwpHcGF"
    b"84ELKV7fo/pv5r1h5s/AYx7/iBM0cws/0MkpPccUt2XiIOIlVlFQw3WCtI5H9DEpItnCGDc4"
    b"insKxzHlJLFvL3d4RvFd4a/LrvCQS/Z3FBig8VPB4c65hiEWWFYaK2RPuK8qKjdlgB5eE/vf"
    b"wzFDF6Pyyd/QxgvWCcJ5xE97tqRl+3tcJE75JZ2QnuWUNnGaU1iJDUKqGvOJPKhrAAAAAElF"
    b"TkSuQmCC"
)

icons8_scatter_plot_20 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAAAXNSR0IArs4c6QAAAARnQU1B"
    b"AACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAAGYktHRAD/AP8A/6C9p5MAAADtSURB"
    b"VDhPzZS9EsFAFIUXjU5FT6FEpVFTKAyFFzKeAk+g1niJtLwFJYbhnLtZk2wiNkuRb+ab7Nlk"
    b"bvYnG1V4SuHV0IVt3XTmBvfwIilCBz7gM6dX2IcJ5pAP/EQ5vP6NrIIreIYzSY5kFeQS1OBY"
    b"kgf2Gk4gR9mU5DHib5tygry/luSAXbABR7AiKT5i9g0hn/mIXfAAmZeS4iwg7x0lRcjaFFM8"
    b"+hJDWl8Ce4R1yGmZKU8h168FvaZsYzZlI0nDs0/f5DkpW8jPZidJFwpCe+yw4fd1100nWJA/"
    b"ExobpaEKB7rpDP9QqcWKilIvu2w5UIty+GoAAAAASUVORK5CYII="
)

icons8_bold_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAD"
    b"t0lEQVRoge3ZS2icVRQH8J/axCrUPrQ+qlB1UaGCSuqLilAUEbTUggtBpRVR0o0ggqBkZTfi"
    b"RisKVUGh4ANd+IAspCqoGBdVWkUqVtCurFip9RFN0gTHxbnjTGK+b+4kXzKDzB8+zsA9c+45"
    b"37nndT966KGHMpyUwXMedmFVRXv+htFED6VnH/6oSH4h7kNtgZ8JvIftOGUuSuZ4ZAd2YxhP"
    b"z2WTGViO03AWLsF6XIv+tP41BvFJBXtNww7x1nZXLbgJy7EN36a9xnB71ZsshiF19OHJtN8k"
    b"rsj948kLpdEcMYmH8AyW4MVEWyKLKQNLsaYFzyiOZsp7FFswgFvxztxVayDnaI3Iy04n8B2e"
    b"E4Fehp3pP3vmofs05BhyPPEcForO9hw13agx3FEi8+rE99X81G+gHUNWtJDVh43iLdeNKfLM"
    b"2YnnpxwlFzvYJ/GpKHx7RGwNFvAew984U4aencxa9bN/ZcF6TaNg11oJ66QhxxJdXrC+Rhjy"
    b"sy43ZG2iPxasX5folznCOmVIvyh88EEBz/2JDucIrKog1rFCcSPaJ7wwIIxYJ7zxwiy823Gj"
    b"OH4v52xctSGH2+S9TcwlzdgmjKvhQfyaI6wqQ97EVuVjwRR+EYPUsHjTY03ra/EsNgsjHpHp"
    b"jVwsRve7UhhZE7WjrOLPim7pfsfELEJ49THc3I6AbjFkXEyJG/CqSATvilOQNfpWFSMX4qoM"
    b"vnER3Ac1CmIz9uMuvITXxbGewgNVKJkTI/URtZ1nH+5UnCAG8GfivaGVklV5ZHWib4vGsAhL"
    b"RRN4mfDgK2KAulu8+WbsxxCewhPyPF6KKtv4Ok7FvRqZaqiArw9HEs/lZQI7FewTIg62CiUf"
    b"FkrPxCTeSL83lwnsdNb6GF+IDrjo6IwkWtTuo/OGEBdyNLrhmfg+0QvKhHSDIfUg7y9Y/z3R"
    b"0vjrBkPWJVo0l6xMdKJMSKcN2YhrRL0YKeCp35eVXkJ0ypBl4pZ/OOmwSxgzG9YnerBMYNXz"
    b"yFv+W9iasQzn4xyNdPuaaBKLUL/Mfn++yuUUxEPaa0+m8GFSsmyG2ZL4jyhOBqjOI9eLtqMV"
    b"RvGDOO8nWvCuxvPp984M/pZYzM8KdZyLz9O+e2V8kOp01poNN4nbyA1irr9Hl99rNWMJbhFZ"
    b"bC8uEq3LJhEfWQJycQYubk+/WXG6qNKrcKmYOzaJb4pEJX9cpOTxCvb7F4MW/qtuTdSJIZGa"
    b"20aORz7CAcV3tO3iLzG/HBffTQ7gM3xTkfweeujh/4x/ALbGH+I/qO5zAAAAAElFTkSuQmCC"
)

icons8_italic_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAC"
    b"LElEQVRoge2ZTSuFQRTHf14LKZHIRpSFknKFFSI7G0ufga/mI9goG9d12SgLShaKiPKW12tx"
    b"ZrrjGlceZ+bpqedXT3Pvv+495zTnzJmZB3JycurREMnOOrDi0c+ANeA5kh//ohV4Aio/PKPp"
    b"ufY3JhGHT4El86wa7QFo1jCi8ie/MGPGbWDTfF42Yxl40zDSqPEnvzBlxl2PVtQyEiOQaTP6"
    b"AtklI3QC78AL0OboF0iNDKfhVBIWEIf3HG3YaNcoLv+hU8umVdGj7SABqRA6kCiFDvFmJNOF"
    b"3o+kzj3VftVkvleAPk1jIWfEzkaJatMbAzqQLn+haSxkIL5a8BW/CjECyXR9NABXSC0MOvqB"
    b"0ebTcCoJI4jDl47WDrwinb5T22Co1LIptONoBWT1OgTutA2GDsStBV9PUSNUIL7VKXOF3gI8"
    b"Ah9Aj6OfIHVTSMOpJEwgDh87WjcS2BMSqDohUsuXVjPIkryPrFzqhAikXqGrd3RLrBnJXKHb"
    b"pveKbA4t9mg7koZTSZhDHC472pDRbgh4s6mdWvUOUkUUj7a1aAcS7WhbS6hAfGeQzBR6L9/v"
    b"c5uQDWIFGEjJrz+zjDi85WjjRjsLbVwztVKrD4gXSGbqA6pNb8jRykZbTMWjBNj7XPdo24Zc"
    b"Xn8AXaEd0EotXy0UkC37EXCrZOdHtAOJuuN10Xr1ZgM5p/rOY9aMJSUbUbBNz/dM1/mdGloz"
    b"soHsfGsp8fUlT05OTs7/+ATr8IVDpqnfoQAAAABJRU5ErkJggg=="
)

icons8_underline_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAC"
    b"dElEQVRoge2aQWtTQRDHfxWqBatIRWirRSu29KJIVTz10LNKToJ+BUX6CRS8KPgBBMWTB1u8"
    b"txdFQakerEhPCmqFinq1NoKxvsTDzLrlJZV5ySZdZX+wTHbe25n9Lzv7Ql4gkUgk/kceAbVc"
    b"e9qGPPPN5ukyJqi1ON5K03m2FEzUZQkagMJ5igqJliQkNpKQ2EhCYiMJiY0kJDaSkNhIQmIj"
    b"CYmNJCQ2rEJ+qu1VW871Q7BT7bdcv2IZbBXigg+q/ax2wDjeQr/aL7nYK5bBViFLueCuP24c"
    b"b+GY2vdq3aItNbi3DquQRbUTamfVlozjLbhYLrbLtdjg3qY5h/x49kL7Q8Av4AewP0D8YY21"
    b"BuxT30vNeTZA/D/sAL4DVeCQ+u5oonsB4t/XWLe0P6q5yoQ9UAA/8Wnt7wVW1XephbhTGmMF"
    b"X4NO2O0W4m7ICHIMV4Hj6isBGbIlmhEzhWzRDDijvpOaowIcbGG+f+UGslJvgb51k8nUPwMc"
    b"MMQZxq96hl+E3cA79V8PNelG9ADPNdEDoFv9JeRZU0OKdho5IMaA7drGgPOI2Ap+O53WGN34"
    b"1xfzwLZ2CgF5cC1rwifAHvUPIsW6Rv07jnzLgLv4mugDHuq1T0j9dYQjwEf8Njux7toQcBGY"
    b"A14jB8Kqfp4FLuCPWJCacNtpGTjc5rnXMYDfZlVky4wUGD+K1ElVYzzDf03pOD3AVeS8d4IW"
    b"gMvAJPU1MglcQR52TkAFuEYHasJCP3ATL8jSykhNBTliQ79G6wVOISt/FDlmd+m1r8AH4BXw"
    b"GKmhcoMYicS/yFbgDfZCDtXMf0oo8uPDRi/z28lm5NxcfgObzr2fydjmggAAAABJRU5ErkJg"
    b"gg=="
)


icons8_camera_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAD"
    b"fUlEQVRoge2YTU8UQRCGn5j1ICwfiXjBRC8iGg+i6NGIGlFCAsKP8AcYlagJQUGvft80XrkY"
    b"DZ5wMTEQDiaCXhSvApGDUeQ7UWA8VDUzkN3Z3pleVsy+Sadnpqverpqu7q5uKKKIIgqBHcAN"
    b"4AuwDHiWZVl1ritHQVECvMXe+ExlGCjbXNPX47EaMgU0A4kcdBOqM6Ucj+IaM0z43xrKoLcH"
    b"+A38AQ7H6L9OOX4rZ2TYDH06dGpbb5zOFb3K1RlFuQS4SLixNk42Rul8AxrT8M4Do8AtYFcm"
    b"xQZgPKD0LoPcUIgDHjAIbIvthnAMhvQzA7RvVDqHxKMHPAdOkNsk3SyUIj/8JWLrCtBmGquA"
    b"79pwqQDGRUUHYvMvxAe69MObPHZaqx0PAGNIrM/rcwq4CuyPwNuH2H4T4KO+nAwINAOTwATQ"
    b"FM12AOoR4203wQHVscUp1RsFWNCX0oDARIB8PIIDCeAhsKocP4AnQAsyOqVaaoFW4KnKeKrz"
    b"ALs5WqY6swQMDiKOI5VImHrIT+oGyi30yoEeYBF/dCot9NbsT+dIE+LMOHDegsxgO74T48CR"
    b"HHQN6vF/ZIrsIxPqSFQ8xHeiOgZPNb4z97LIOnekHonvBaKNxEYcRcJsJQufc0fM6tTtgMvg"
    b"tnK+DpFx6kgt/upkM7FtUQH8VO6aDDIe4LnIicBPE16gS6EjzCDpCMCFMEFXjpzR+pUjviAM"
    b"59kwIVeO7NX6kyO+ID5rnfWA5WKOzClHMiZPOiSVey5Du9M54mofSgdj46qNUFxMaR1nE8wE"
    b"w/ktTMiVIyYfO+iILwjDGZrzuXIkpXWLI74gWrUO2xSB/2RDXPcQEyZF6XHAZXBHOftDZPKW"
    b"NC4iCV9cHAOWkKSxLkQuL2n8A+WaAHbH4NmNn8bfzSKbF0cS+CE2CRyPwFEHfKXAByuQ42lK"
    b"OReRVLzCQq8CmRNL+Kl77KNuXCSA+0h8e8jK8wzJYA8gaUdSn9u0zaxOK0g42V4Qrtk/S/7y"
    b"pENI9mp7HZQit4WiHP/6lA/60uDE9PSoAa4g4TKGJIBzSGbbD1wG9kXgPY3YPgJys+3hH2C2"
    b"Esxod4Fcz8/oh47C2ZQzriE2TwM7zcd2/InZh1xF5mPOxEUSCSczEiv4udga2pCbbduJWegy"
    b"nc4JgyrkZnsE/9T3L5VZ4D0yJ9bCqYgiiihi6+EvESa3u9XaFVMAAAAASUVORK5CYII="
)

icons8_detective_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAE"
    b"tUlEQVRoge2Zb2jVVRjHP1eh0nStsk1tumYJScIKCcI/s15EqETEZjgXZNGLwJIKp6KZoIXa"
    b"i15J0KuyKGTYH2dK0YvKUhFLgsiMqBSZkhNXs7np7nZ78TzH89u553d3f/f3u/dq7guH391z"
    b"zvOc5znnPH/OGYxgBEVBKib/RGAhMB+YCdQCFdr3D3AC+Bn4GtgL/BVzvsTRAOwG+oFMnq0f"
    b"aAfmlUHfLNyJrKxRrg/4HFgJzEF2ZKy2WqW16pi+AN9nwLQS634ZLcB5VeQc8DpytPLFJOXp"
    b"UhndQHPCOg6L1djV3ANMjiGrGvg4IG9LbO3yxKs64QDwfIJyX1CZGeCVBOV60YJ11JYiyTcB"
    b"Y0kR5APi2MYnXi7WJCrb+ExdoUJy5ZG9wALgE6BRJ3MxAXgImAXcDdQA47WvG+gAjgFHgK+A"
    b"zhAdPgIeR6LZo1GNyIUGVbyHbMeuAJ4D9mPPuGlG+Q79HewbAA4Ay4GbHJmTda4MMDdJQ3ar"
    b"0M0BWiXi+OcCih0GXkMy+60eObcgi7IJOASklbcL2OjwbNa+XUkZMRFxwAH9fQOwAfgbu7oX"
    b"gPoCZN/P0MTYjSzEGJ0rDVwCqmJZoHhGJ/kGycy/6N+nkB3IAKtCeBuAddrCShETzo8gPpMB"
    b"fgMeRGqyDLAsrhEA21XYn8iu9CKrNg44ihytGx2e8QwtXYKlyDhnbAWyuz8hx/VNZBcGgZPK"
    b"904ShvwQUORHpKoFiUoZ4AMPz4ceI0x73zO+Tfum69/1SJVseA4nYAdnsdn2+gB9kdJXOOPv"
    b"QFYzzJBBYKrD85L2LQzQxgDblH4mqtKjPDSTB94ALgbot+vXvVPUkzsfpYB7Hdpp/dYEaL3A"
    b"i/q7gojwGRKGPv2Odeg9efD+6/xtZPQ59NH67Y+gF+A35Lx+3aRlVtE9JgcQ5w1DF3DQodXq"
    b"t8OhV+o3kZvk98g5fcCh34xEl/0enmcJ95GnPeMPIsfWXazZyvNdgboPgQm/vkLxSyQkz/D0"
    b"NSN3dGPAcfwV7T0q4wtP30rlfTuq0j6YhLjP0/eI9rWH8KaQK+w0wgPAHpXxsKfvW+1rjKBv"
    b"KKoRZ0vjLxVM4mstQPYqbKJ0UaVz9mN9JTbaCb+GTgD+QPLDOvJ7UkoB65Xnd/wF5lads60A"
    b"fUMxD1sc1nj6pwO/MrQmC8Nc7JE5BtzlGTMFySODZOec2DClfBv+Va9Eyg9zJzmOBIpNSG22"
    b"XWmm5H8P/5FJATt13KcJ6n8ZddjL0Zoc4+5DosxpskPvKe3LtcprdWwn8V5ncqIZu6KLhxk7"
    b"Cnm7mqVtEsNXDk9gd/SxWJrmgfVYY9YQ/70YlbEWa8QAxXmlyYIxxviMLwDkiylYnwi2NLA0"
    b"npr5YQnWZy4goTnKlbQKCbG92GuuucMHjSnJM2odNpqZifchpcVsJJlep61aaa1I+A0qvQNx"
    b"7KXlNAYkN+wi2r8VLiK3S7cYDTOmaC+PPlQBTwHvItfTTkThHqSAPAS8pUrdlkNOM1eAMUlh"
    b"Mdk7nAaeLKdShSLMmJKE5qTxvzKmiWvAmJIkzaTRhLwTXDvGRHnXKhd2Ir6RDtBG47+gXRVo"
    b"xO7MhjLrEhtNSCU+ghGUCv8BPlKp3kSlWv0AAAAASUVORK5CYII="
)

icons8_picture_in_picture_alternative_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAA"
    b"qUlEQVRoge3YUQqDMBCE4bF4/0tpz2WfIgmY4sNunMj/QZ+EsrMxsKsEAHjYV9Ix2W8rxS9V"
    b"kCOmH8MtkrT2HkygafznqSqiEcQNQdwQxA1B3BDEDUFuil4NNnVcjfGR02/GalDqa+q9GuMz"
    b"RDTnb1O4I24I4oYgbgjihiBuCOJm1NCY/oE8+0T24P/r7iO1srzMoqn31XdkplM51ScS/T6P"
    b"cOvOAADS/AAtmFEkt1mw4AAAAABJRU5ErkJggg=="
)


# ----------------------------------------------------------------------
icon_corner1 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAAAXNSR0IArs4c6QAAAARnQU1B"
    b"AACxjwv8YQUAAAAJcEhZcwAADsQAAA7EAZUrDhsAAAAGYktHRAD/AP8A/6C9p5MAAACFSURB"
    b"VGhD7dhBCoAwDADBxP//WT30AZGWsK07F73JQkKLeb/iANd4bs8QGkNoDKExhKZ8smfmeOtV"
    b"vXg4WjSG0Ewte3URq2a+4WjRGEKzfNlX3wBc9l0ZQtOy7NWFneFo0RhCYwiNITTHhLT8oPNk"
    b"/8AQmv8tO52jRWMIjSE0htAcEhLxAPHmNEI9nLL+AAAAAElFTkSuQmCC"
)

# ----------------------------------------------------------------------
icon_corner2 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAAAXNSR0IArs4c6QAAAARnQU1B"
    b"AACxjwv8YQUAAAAJcEhZcwAADsQAAA7EAZUrDhsAAAAGYktHRAD/AP8A/6C9p5MAAACESURB"
    b"VGhD7daxCsAgDABR0///59bBsUMgoKfeW9pNDgwx3q4d4Bnf7RlCYwiNITSG0KQ3e0SMv7my"
    b"Dw+vFo0hNKVhzw5iVuUMrxaNITTLNvvfsQ57ZwjNfcNekR1ih70zhMYQGkNoDKFZttmz3Oy7"
    b"MoRmyrDP4NWiMYTGEBpDaA4Jae0DIcg0QqlRrDkAAAAASUVORK5CYII="
)

# ----------------------------------------------------------------------
icon_corner3 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAAAXNSR0IArs4c6QAAAARnQU1B"
    b"AACxjwv8YQUAAAAJcEhZcwAADsQAAA7EAZUrDhsAAAAGYktHRAD/AP8A/6C9p5MAAACJSURB"
    b"VGhD7dnBCoAgEABRt///5zLwJB42BBtlHkTdaqhFobircoCrnbdnCI0hNIbQGEKzZGWPiHb1"
    b"Xfbx/LRoDKH5LeQd4v6Y4RuhMYTGEBpDaI4JSW/jZ7biI6Pbju6RXfH9tGgMoZka9uwgZjns"
    b"lSE0DvsqDvuuDKHxPzuNITSG0BhCYwhLKQ/jczk4U5txtAAAAABJRU5ErkJggg=="
)

# ----------------------------------------------------------------------
icon_corner4 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAAAXNSR0IArs4c6QAAAARnQU1B"
    b"AACxjwv8YQUAAAAJcEhZcwAADsQAAA7EAZUrDhsAAAAGYktHRAD/AP8A/6C9p5MAAACLSURB"
    b"VGhD7dnNCoUgEEBhp/d/537AVbgwJvQo54O4bSIOKQ3dOG9lA0f9XZ4hNIbQGEJjCE33mz0i"
    b"6tl3I4YHlxaNITSpkGcTv49ZfCI0htAYQmMIzTYhqTG+dWlm3G/pnRZcWjSG0Py+2TMy93Bp"
    b"0RhCM+QDXYabfVWG0Pg/O40hNIbQGEJjCEspF8w6OTgLmXHlAAAAAElFTkSuQmCC"
)

# ----------------------------------------------------------------------
icons8_down_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAA"
    b"9UlEQVRoge3YOw6CQBRG4RM3gGBL4cZdhZ2JhZ1vKysLl4IFTCCEx4ijXMz/JZNQkOGeZkgG"
    b"REREbNsBp7GHCCEr1lfNvv2BX1GINQqxRiHWKMQahVijEGsUYo1CrFGINUNDVsAVSAPOkgJ3"
    b"YBtwz15r8guFB/0xPpcPabFXBmw+nu4NEbAvPvwElh3v9oVUIy5AHGZEf74xXSH1iCTsiP58"
    b"YtpCzEQ4fTFNIeYinAg40BxTD6lGXDEU4bTFVEPMRzhNMS5kMhFODJwp/zNZ7fnMCEfsUHPg"
    b"SBnh1g1YjDjXIPWYSUY4CfnxauqIHWpeLBER+T8vFihWmFWiZgQAAAAASUVORK5CYII="
)

# ----------------------------------------------------------------------
icons8_down_left_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAA"
    b"yUlEQVRoge3XPQ6CQBRF4RP3IHH/OzEWhsJGCpczFkDA+MeM6NwX70leQQF5X6ZhwDnn3Po1"
    b"wAnY117kkxqgAxLQVt6luC1wpkdcgF3ddcoyQiUjVDJCJSNUMkIlI1QyQiUjVJJBtMCx8N35"
    b"9bQbnquVhslN5iTGSiByCMiHSCIgDyKLgOUQaQQsg8gj4D0kBAJeQ8Ig4DkkFAIeQ8Ih4B4S"
    b"EgG3kLAImCChETBBZP5iS0uzCXkSY2mFOfxq2c2Xv19yn3HOuT/oCq/olcDrAa3nAAAAAElF"
    b"TkSuQmCC"
)

# ----------------------------------------------------------------------
icons8_down_right_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAA"
    b"v0lEQVRoge3XMQ6CQBRF0Rv3IIn734kWRmKlhcvBAhsCKMzHzPvk3WT6dzLNDDjn3F46A3eg"
    b"qT0kWgt0wJPkmCPwoMe8gFPdObGMUc0Y1YxRzRjVjFHNGNWMUc0Y1XaFaei/y9Fv8w24bjWq"
    b"tC1upvuc6kUxMhCIYaQgUI6Rg0AZRhIC6zGyEFiHkYbAcow8BJZhUkDgNyYNBL5jUkFgHpMO"
    b"AtOYlBAYv5rTQmB4MzKQC8NBpWeywx+HO+ecm+0NpQGU2ZDuCLIAAAAASUVORK5CYII="
)

# ----------------------------------------------------------------------
icons8_pentagon_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAD"
    b"HUlEQVRoge2ZSU8UQRTHfwPjAi5xwT2SqBeXxMSDJ/VAMNGRGAQOIiae5WTCJ/ArGL6BJt7g"
    b"YEIMaozbQbxoPKAHLjBAxC1KQFDU8fCq0j2dmV6ruoc4v6Qz0+nX7/27q+rVq2qoU2dV0gFM"
    b"A0WgkLGWRBSBkjqmMtYSixwwgPMQ+hhQ11YFO4ARHPGf1KHPR5RNTdMGzCCCvwNXXdd6gK/q"
    b"2hxwPnV1IcgDN4HfiNBXwKEKdq3AC2XzF7gFrElHYjCtwHPKxa31sfc+9Bhw0K7EYLqAL4ig"
    b"D8C5CPe2IalZd8Ne4+pCsB5583oAjwK7Y/hpAe65/NwGmg1pDOQw8EYFXgZukDylXgMWlc9x"
    b"4HhCf6ECLqiA74ATBn0fA94q30vICzLOZuAu5V1gg4U4TZR32WFgqynnJ4EJnEHZZ8qxD904"
    b"c84kcCqJsxzSvD9x0mSlucEW7rS+gqTshqhOdgL3yX7i8s45j4G9QTfpknsGKSFK6rzNlsoI"
    b"uOecOURj1aWBu+QuIfm9JRWZ4fDOOVWXBtMeg1ost3OUv/CivuAePP3AR/X/jjKsNXTqB9F6"
    b"vZphlzJ+loKouOhMdsnPqAmZuf8Ae1IQFZVdSAZbxFOTefPyEpJ2G4DOVKRFoxtoRFaZP4KM"
    b"e5Gme2hZVBweIdouhzHeiLTMCrWVfrcjmpaR2q+MSlP+AtIaeeCiVWnR6EQ0jQLz3ovVapdh"
    b"9dttSVQctJZhXysPW5BisWIzZsAmpLv/ArZFvfkBMrCuGBYVhz6cJXVF/MriIfXbY1JRTLSG"
    b"IV+rKrgnHxurwbA040zScTY4AHiKNGmWg75HaXjiZxS04tJNmeWD6NixupVmH7JCnEf2stJm"
    b"HfBNadif1NkY0rQXkjqKQYeK/TLIMMxiPsvslShbeTmAvJXPSImQFnmc7yrGdm/0Fmm7KYch"
    b"OKtivg5jHHafKIvuZbRbaY7ifDpoNOm4Cg3ArIp5xLTzceX4tGnHFTijYr234XxQOZ/F7ve/"
    b"Ak5rDNoI4N3AS+OYDCsu8qZwyljZJCwgrTKB3TTcrmJMUaOfsOv8V/wD9srxvK1koPwAAAAA"
    b"SUVORK5CYII="
)

# ----------------------------------------------------------------------
icons8_pentagon_square_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAC"
    b"xElEQVRoge3ZTYsUVxTG8V+LiBJBcBQdiLpRBFEEFcWAm+gsXPqyUYkvn8ClGwVB0J3iQj+A"
    b"KzejgbgRXWnIqLNSFzMKAyIYlYRAENHEl3Zxb9s97VR3163qHpD6Q9FQVeec51Tde+651VRU"
    b"VFRUzAK1LtfrA1HRO930ZlI0kSPRRx2/FPRVSEsR42UY10xkPJ6bDS3JxiN4iU+4GY9P8dzI"
    b"gLUkGc/FaUH0a+xuufYzXuAzLmJen7UkG6/C79HmFoZnuGcpftMcaqv7pCXZeC/+wf/CG5nT"
    b"4d4ajuM9/sXBkrUkGc8Xhkkdk9iUw/d6PI62V/BDQS3JxuvwqEXIwgT/CzQfxAQ2JmrpSpbx"
    b"YbwVhsahIgEi+4Sh+U4YdjMtfKUmsghX4/kH8k3WbrQWi+tY3EVLLlqNt2JKevnshdby/Rw7"
    b"MrTkpo4TOIMP+BM7izjskZ0x1ocY+4QCiQxpthd13BDWgUGxNMZs1TCU4mi4xcETBTrPAtTw"
    b"tEXH8qwbOy1cL+PvfxgzOy19HX9EDfCqiKMb+FuYiINmLv7SbGuSqeNY/B3EJG9nV4x9VAmJ"
    b"DAnV41JhWfm5HGMvUdI6cluYM53mVNnMEUrwrTYtmTf3wqhQMban68rNT0LlHC3DWeMpLMNH"
    b"nC/DaY9cEFb4xr6mtBblrtA2DGI9qeEZ7mRo+YY8Y34UK7A5t6z8bBGayFKGFdOfwo9Cw3i2"
    b"LOcdOBdjrczQkpt24wdCy9BvJnG/i5Zp5C2n17BG2Kb2iw1YG2P1TN5EGmN2X067PDR8/1qm"
    b"05le56N49IvHeNijlq+krNSjmq+/bBrDNne1Sk0E9iTYdmN/W4zSyHqdE0IFK5txYROXR0tP"
    b"ZBmfF+r8ySLO2zgVfWa1QX1J5J7pe+kyj7GURFJ3fVPYhjea37mKUMMB4WvlVKqDTnw3f71V"
    b"VFRUVPSFL5FE0S7qGwl3AAAAAElFTkSuQmCC"
)

# ----------------------------------------------------------------------
icons8_right_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAA"
    b"o0lEQVRoge3YMQrCMBxG8ad0V3TtsTykJ/AODrEObh5AHL2AOugkIsUEEv++H3QN3xtaQkGS"
    b"JElq1BrYALPaQ3Il4AZs+fGYHjjyiEnAou6cPGFjdhjTjteYZd05ecLGDBjTjuIxE2D/PLDm"
    b"k4D5p6HTESHXkdF6I8R7EuIzbEQrQty3QlznjWhFiAiAA4V/PnQlDvnCGTgBK+BSaYMkSZL+"
    b"zR15m194agQJmQAAAABJRU5ErkJggg=="
)

# ----------------------------------------------------------------------
icons8_square_border_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAA"
    b"7klEQVRoge3Z4Q6CIBQF4GNrPlQ9X1nvGb1G/UA2t+wKFxCB821tzTa5cBSRACKSDCvHPgnO"
    b"oRHV7ilREcWdhd+2Rjp0BH2p2u0iESfXyIe2JybVVSJOqtkp9PxeV0QzibAjRyPdI3vPVlvE"
    b"eppJhIiInBHAE8AbgAEwzceq84B9iC0/96IVKRnY4i8ArvN3k6uxPZ7sy+X50ZY9Xib8Xlq3"
    b"ohUpjbCdMQBesJ2o8mYnIkovZDc+977WP171NPPOLnVkQLkU1oj1dJFIVZrpSMhufO7ZLGqJ"
    b"31UiUf9bKKgS7iKRUq+lqnabSYSIZF/o3CVWfRkALAAAAABJRU5ErkJggg=="
)

# ----------------------------------------------------------------------
icons8_up_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAA"
    b"8klEQVRoge3XsQ6CMBRG4RPjDurK4Kv42ro6qEGdmBxceA8drKmIKJZIL+Y/SROGAvcLCQRQ"
    b"Sin1p6VuDbopsHdrGnmW4FJgB1zcOgKzqBMF9IwYJGYC5NwGP+ER9+Pc7TFdCmy5DXwG5nhI"
    b"hsccMPxkEuoI8BCoY8y9AJoQUIWAYcw7BNQhYBCTABuaEfAaAlVM1O9MGwQ0Q8AApi0C3kMg"
    b"MmaF/zZkH/Z+gkAVswwZaBRykjuvABZAGXiNx0p3raLDTD+vzRPpnFn9twliLUGsJYi1BLGW"
    b"INYSxFqCWEsQawlirXEP91jTwz+7Ukop1aUrdgdXo/8Mk5oAAAAASUVORK5CYII="
)

# ----------------------------------------------------------------------
icons8_up_left_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAA"
    b"w0lEQVRoge3XTQrCMBRF4YN7MOD+d2IHBXGkA5dTR4Eg/rRpa+4L90DpKOF9yaQF55zrpWmD"
    b"Z/jXsIed95923n9W5ck+gFPbcerLiHvxTk0nqixDjsCNwDeTIRAcU0IgMOYVAkEx7yAQEPMJ"
    b"AsEw3yAQCPMLAkEwcyAQADMXAuKYJRAQxiyFgCimBgKCmAE4V65NdPDVnJO7mTUZo5oxqhmj"
    b"mjGqGaOaMaoZo5oxqnWFKX+bL41nWV0CrsDYehDnnNumJ/0DldujWquLAAAAAElFTkSuQmCC"
)

# ----------------------------------------------------------------------
icons8_up_right_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAA"
    b"vUlEQVRoge3XTUoDQRSF0YN7MGT/SzGDDHQUBy5HByEQpNX+E2/J/aCpWfMOb1JFa6216U54"
    b"3+Gb7OEXB293PeJixkaSO+DVdfjbORzkfhNvOBoQMoVgMMhXCAaCfIdgEMhPCAaAzEEQDpmL"
    b"IBiyBEEoZCmCQMgaBGGQtQiCIFsQhEC2IgiAfL7FHlb+54SnvYZa2h6b+POKSKmIlIpIqYiU"
    b"ikipiJSKSKmIlP4FAp5tf55GdMaLwRGttZbZBwfblLXkvxCIAAAAAElFTkSuQmCC"
)

icons8_left_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAA"
    b"mUlEQVRoge3WOwrCQBRG4YMbmCzBrbsGS+1sfGDlAlxKLMLtBCEjucPlfJA2/AeGYUCSJEna"
    b"UAOOwCF7SI8G3IAZeCRvWa0BV5aIN7BPXbNSmYg4TkZkmjBiDBNwx4h8ZSKeLBGZ3+XX0F1/"
    b"6ybmf/ykxNEKJa7dYMyoSryzQonnezBmVOVi4gJ4JW/p1oATcM4eIkmSJH31AQ6pXcrw+RVm"
    b"AAAAAElFTkSuQmCC"
)


icons8_compress_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAAAXNSR0IArs4c6QAAAARnQU1B"
    b"AACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAHKSURBVGhD7ZpNSgQxEEZnpd7DlUtd"
    b"ewPXHsITeCfx/xe8kzcQtR5OQ1GkeyZRqC9DHnww0yjUo7rpJDWrwWAAB5aj3495HFrO1znl"
    b"QiX7ljfLh+WEC1lcWL7XeeZCBUi8Wqb/RyatM60iexYvQegMt1kKLSJIvFiiBB1Ko1akJEFn"
    b"UiWgRgSJJ0uU4Ho624qUJPh7CQnYRoRiHy2yErBJhGIfLF4CKSkJWBKh2HuLvATMiVDsncVL"
    b"0BlJCSiJUOytxUvQGVkJiCIUe+OuETojLQFe5N1y7b4TOiMvAV7ky30mdKYLCfAiPnSmGwko"
    b"iXxaeC6uKiOzH/lrzixp7IzIseXyn8K2edAdtK3UzpZwO6XBg1R6wFrCA57Gzojwsim9hJbC"
    b"S42Xm5RILSwv4gKwOxEk4lLcLwi7EEEiboroDEv0bkSQiNvTaSnOpqkLEYqNBwV+U9SFCMXG"
    b"I5u4PZUXodh4eFY6KJAWKUnMHdnIilCsL44sHZ5JipQkOGCekwA5EYqNkyKKXJIAKZE4syMM"
    b"XTZJgIzIND1tkQAJEQaMUaJ2UiQhwsiX0a+XqJ3Zydxa7EeQaZ2e8mOA6YcB6acddCZtjj0Y"
    b"yLBa/QCFElub65nNHQAAAABJRU5ErkJggg=="
)

# ----------------------------------------------------------------------
icons8_enlarge_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAAAXNSR0IArs4c6QAAAARnQU1B"
    b"AACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAEVSURBVGhD7dldCoJQEIZhr4r2EBHd"
    b"d9Xi21VELaDOCwki/hznTMcZmRe+i4SEB8JEmyiKomhL7dJuyjukVe+U9lHeNa16m4Ec0x7C"
    b"vdLMQKTt0+5priFTCOYCMoTg87vz2TxkDMHxZ+eYacgUglxA5hBkHpKDINOQXASZhSxBkEnI"
    b"UgSpQbiLvfx25oAwCYLUIHy5PREnlSRFkBlICYJMQEoRtDpEA0GrQrQQtBpEE0GrQLQRxCW/"
    b"vfzzVyAuF/IPhGo5EPMImoO4QNAUxA2CxiCuEDQEcYegPsQlgroQHs24RFAX0p8bBI1BXCFo"
    b"DMKD5qEH0DnjAXf1pn5a0vHKoXqbgfC6a+g1WMmK7mKjKIoiQzXNF/nEYloeaSPOAAAAAElF"
    b"TkSuQmCC"
)

# ----------------------------------------------------------------------
icons8_rotate_left_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAAAXNSR0IArs4c6QAAAARnQU1B"
    b"AACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAANgSURBVGhD7ZlLyA1hGMePO4Xo27gU"
    b"uSwkt5S7FDbuC5KiWLmVz20hsVZkoSgLOxulSBELt40Fio1yXZDLQoqk3In/75x56u0035mZ"
    b"875z5pyaX/06c55v3need843720qJSUlhTJTrq8ddg7T5GE5uvqtxmn5r3bYGZyTJIxbCUQk"
    b"NeSEvJFBzg/OoOgTtkhryCUCEQflg9phLHeklUsj5wdjmDwvb8peBER/+Ubek3sIpKSwhgyW"
    b"L6RVvFkaQ6PPLDRqyFm5rc41MhhHpF3sAgEP3Ia8do7xq1wmg9Iv+gT+nbhbh6JjH9yGbJLd"
    b"8qcTozFzZBBGyGdydfVbWNyGbCQglksaYPEPcoz0gjtOt0eFf2SWBzkNcQ2BpdL9ZW7L3rJp"
    b"uBNvpVW4W4akp4bAdml/wx3SC3ojBjZ3fAhFo4YA17S/v5dDpDd9os+QJDVklPwi7ZwDMhMk"
    b"fUbOqn7Lj6SGwDFp57yUmZ4Veg4rfI1ATrhzrSUEYhgpf0nLZ7FMjU320HfQC4H1nHicQFoW"
    b"yVPyuezpJ28l9FjWkIcEmsF39A4BCzRryA/ZV3YkzK7d52SiTGSSPBq5l0CbwDhiDZlPIImV"
    b"0go8ItAmMN+zvOhVE3Eb8phAm/BEWl4rCCSxUFoB5lntwjtpeZFjIjxIVoAZLw9a0QyU5GJ5"
    b"jZOJ0LW5U2i2eYpmhrR86H5Tz/vuSyu4i0DB0HtaPncJpIWu1wpeJ1AwLKwsH/YMUjNXWsG/"
    b"0nup6cFYSQ6WT+YZudtv57LDlxLmfJYHXXBmdkqrgM0A7kyroXf6Li0P9rYyQ5fnrtevyFbC"
    b"ZJW1kF2ffa+mh4IN0ipC9p1axX7pXnut9IJfwipjfMljf6setkbdATDIxkeXdLczeV5Wybyg"
    b"bneD7pUcLoMwVX6WVvlvySAVctFFXfskddt1uCbXDso8+UnaRfCqTDXvSWC8dB9s/Chny1yY"
    b"Iut3zb/Jk7KZ7pkylKUOt062fSbLXOGZuSzdCyOjLy9/2B+eLgfIeogxAeScW9Idsc2LkpdJ"
    b"LYO3tbylqk/EpNdhHGI0Ro7jEjf5pdfJQuAOMwN4KuOSSyNlGbHbYd1ThRcyzEx5j8iaIS5p"
    b"5G+cw7l5b8l6w8JngmRJyuszXCDpnfLYDC8pKWlIpfIfTyNhWWO84TIAAAAASUVORK5CYII="
)

# ----------------------------------------------------------------------
icons8_rotate_right_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAAAXNSR0IArs4c6QAAAARnQU1B"
    b"AACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAANbSURBVGhD7ZlLyA9RGIc/d0oiC7Jw"
    b"T5Jbyi2ykOS+ICmKjegr95VYk4VSFFmyUIoUodxKFigLKdeFexaKWLgTv+f/n7dO03zN9cyM"
    b"mqee/uM158x7vpk5t+loaGioBavltPbh/81febR92GKo3Csnt/7lmUPyago5vyvCDdkoieEp"
    b"Aj65Je1iSeT8rrgnd7cPW5yTVm4DgYB+wW+hFNmQMNvlHfla9iYguslr8rQcSKAoVshNIU/K"
    b"qEZgmoYYA4JfWC+trmeyv/TCMvlFusm/co6zNMTljLS69hPwwUz5Q9qFON4i1zmxvA3h0doj"
    b"TwTHRq/gNzcj5XtpCXNXFkpYK4tqSBTL5RNJd52LHvKmtGS5E/Ol4bMhdAi/JXXTCbh3KTU8"
    b"PpYo0v+7+GzINml1v5HDZSboUdxHipcxjO9Hi/GGgdTt3VLDAGZJfpbDZBjfDeHRzkV3+VJa"
    b"kgdkFL4b4jJdHpepGrdAWoI/5RAZBS9+krlWXi5Jy2cxgaQclFbwMoGKcQfLYwSScl9awc0E"
    b"KoZH+Kk8IucRSEJPyeNkDZkqqybTGDJOWiMYAAubIpTNXGkNeUegJuyQ9J44nkAc9ArWkMcE"
    b"asIDaXktJRAHJ1mBhwRqwiNpeS0hEIf7aDHHqQtvpeVFjrGMlVaA2actRaukr7SZMI6SsdD9"
    b"uouoUrZsYmAIsHy+y8TTlLvSCjKVrxp6LMvnNoGk0MVZwSsEKuaGtHz2EUjKLGkF/8jMi5oC"
    b"GCHJwfJhFpwK1spW2OfMNg7mV5YHXXBqOqVVwIYDf5myoXf6Ji0P9tZSQ5fHOGKVXJBlwkTR"
    b"XYewh5Z5KFgjrSLcKstil3SvvVLmgjthlTG+sNfkG7Zr3QGQTYjcDJbu1ijvC9unvghvzb6Q"
    b"g2QhTJKfpFX+SzJI5do0C0FdOyV123W4JtculNnyo7SL4EWZaN4Tw2jpvtj4Qc6QXpgo3ccM"
    b"v8rDMkv3TBnKUodb53M5QXqFd+a8dC+MjL7s0bJnO0X2kWGIMQHknOvSHbHNs7LQDz1x8KWW"
    b"L07hREx6HcYhRmPkOCpxkzu9SlYCf2FmACyJo5JLImUZseuw7mnBxyBmpnwbZM0QlTTyf5zD"
    b"uakngGXDwmeMZEm6KHCOpHfKvTHd0NCQlo6Of9ewYWPOK1cIAAAAAElFTkSuQmCC"
)

icons8_choose_font_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAC"
    b"RElEQVRoge3ZvWsUQRiA8d8lQYyIH6CHBCsV/ACtLMQqEBQrMYpGxcpSELT1T7BSBFsbKytR"
    b"o1ZCCkXETtRgEwlpVBANKDGJOYtNuFxmL3u37N5eZB/YZvZl5nl3bvbemaWkpKRkLVHJqJ8N"
    b"OIgq1sfc78FCBuNMYwwzGfTVwDGMYha1Dl2jWSawCfc7KL/8+plVElWMF5jEtSyS6MfbFZ1P"
    b"4QYOYfOy2G34uyJ2YfFBFM5NjWLPsLVJ7BnhE33fAcdEdmFOXeqNaIaacUeYyN2cHVvitrrQ"
    b"H+xNiH8nTORcnoKtMqUudC8hdrtoPaxcHzvyFGyVCXWpowmxZ4Wz8TFPub42YodxBS/xKiF2"
    b"MKZtrI2xuoYPwhk5X6hRCqrC9VHDQJFSaRgRJjGe96A9OfQ5GNOW+/poZ7GvxgCOoBfHY+7X"
    b"RG+yZuRWnrfDTnzXZeV5Gk7osvI8Lf14hHldUJ5nQR++CSWHipRKw5AwiR9Y14nBs3z9nopp"
    b"W9rPrxkqmBTOyEiRUmk4LExiFls6JZDVT2s4pm1MtEbWDH0aN11L19UipdIwLExiTpfsBtvh"
    b"uTCRx4UapWCf8OyqhtNFSqXhqTCJz7KrqjPhgGh7uqfJ/Yvi66brHbFrkcvqReCcxvOoiuiP"
    b"bkaYxKTVD+06zleNgr/wRHREOiF+Jmq4UIRsMyr4rf1S/EERsknc0l4Sr7GxENMEekXHoq0k"
    b"8VD04aeruYRPQvl5vMDJ4tQaafVj6H7sXoz/Ijqnms5LqqSkpOT/5x8uy2K2p2FyYgAAAABJ"
    b"RU5ErkJggg=="
)

icons8_level_1_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAC"
    b"mklEQVRoge2aO2sUURSAP6OFidkNG2MSBOu0EUERhdjbyZLSTiWFhSCWoiDoT/CFjb1/QAQf"
    b"6xIbFWOTgCDEN2wUjYXIZi3ODutOzszunXPnUcwHp8jd7LnnS2buawZKSkri2OE53xSwABwE"
    b"5oB9wHj3s03gG7AGvASeAC3P/ZuoAktAE2gDnSGjDTwHznVz5MYEcA34zvDFR8UGcJUchBaB"
    b"T4bCo+IjUM9CYAy4l4JAOO4Ao2lJ1JBrOm2JIF4gg4dX9gJvM5QIYgWY9CUxBiznIBFEE0+X"
    b"WRb3xKC4bZVYLIBEEIlHsyoyHOYtEMRnZO5SGYkRuQTsd1KP5h1wBbhoyDELXHD90gT2GfsH"
    b"cm0fp7emO2nMuYHj7L+UsKM28BA4DexR8lpFOsjabGiaCTs5MyCvD5GGlli7R6aAI4NdVf6G"
    b"fq4lzBPHUZRJUhM5EdE+LAeA88Aj4L0hTxQjSI197FJ+cd7QyXVght7N/duQK4554MH/DZrI"
    b"nKGDWcN3XdhWo3YJzWRQiJXpcIMmMq60FY1tc4nlpi4Umshm5lW48zPcoIl8yaAQK1/DDZrI"
    b"WgaFWFkNN2girzIoxMrrcIMm8hjYSr2U5Gwhp5R9aCItZI9eVJrIcr6PqOH3frq1mHCqrYpY"
    b"W5fc4aHcuoxvARWt4J0RIn+QY6CFodV1OsgJ/KFuHAMOG/LdQDZuTlSAD9j/K75iHcPyqV4A"
    b"gSBOJZUIuFsAiZtWCZDjyqR7eB/RAHb7EAHZI6/kIPEGj4fYATXkr5OVxDIpPFYIGEUewqQt"
    b"cQuPl1McddIZmtfxMDq5UkHOc32sAFrAZXLeZleRY8wG7o+nnwFniVh2uOD7hYFJ+l8YmKZX"
    b"5C9kubKKvDDwFGUVW1JSkg7/AOZX0ILb/Rs6AAAAAElFTkSuQmCC"
)

icons8_keyboard_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAB"
    b"nUlEQVRoge3YMU8UQRjG8d+dFDQqNXcUJkhICPYUFvYW9tR8D/wMFNpbGUKFFlDpJyCBykQb"
    b"a0/uiLHCLMXsHRdzkNu93M0smX/yZu4mO7vPs7P77puXTFo8ii1gAm08w1P0I2uZiS4K/Kyy"
    b"qD0fLTOxUo6XVRalaGS7HH9UWZSikdfl+DWqihl5iWv8xWpkLbVYxz7+CC/626hqpmQTezjA"
    b"F+GlLsbiHVqxxE3DlvDcFxPiN47wqu7JF+V8Byd4jAFOcYYLnKv4zYjFMr4Ld/4DnsSVU59d"
    b"wcSZOZZEi/iOvCnH9/i3gOvNjW/CjrxYxMW6OMSVyVklxbgSMt3zcRO9BITVjR46yp0ocDyc"
    b"aAgdfBK0f+T2cWqSiSFrgvZ+q/xB4mXBPRSkWcbXYumO+eK//61E50c8mB3JRlIjZ63UmDZr"
    b"jRMrU006ZsSD2ZFsJDVy1kqNedVaVcm11pBsJDVy1kqNttB8ILSFmsZaOQ4ITa5CaK00yUwX"
    b"nwXth7CBX+I32mZp0K0P3XWEJtcgAWHTxqDciZGJTCaTaQ43WK8NPKELVSYAAAAASUVORK5C"
    b"YII="
)

icons8_roll_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAD"
    b"60lEQVRogd3a3Y9dUxgG8B89M1PpHKLtuBEqqSolbXzFx4UIE8y0IxE30vi64kJk2rpF8R+4"
    b"J5qQ+A+4QLSIdlAXbWZ8lUjRb0GHpF8xLtbaWVv17Dnn7HXO4El21snJ2s/7vHuvtd53v2vx"
    b"P8F5Gbkuwl24HWuwEiMYxhyO4xd8g734FO/G/xcci7ER7+CMILiT62S89yEMtGFvCjtzOnAB"
    b"NuHgWaK243k8ILyVpRjEkPB2rsGDeCH2PV26/6fIOVhht+ibBWP4vkT6GZ4UhlanWIonhKFW"
    b"8H2N+1r0z+LIYrxSItuN8bqkJYxjOnL/iZejzTJqO3KpMDnn8Ae2YFEdwhZo4BmciLamhCFZ"
    b"oJYjK/BtJNiHtV3LbB/XR1tz+CpqoIYjgyXCXbi4vsa2cYkw/wpnlqvhyFAkeQ8XZhLYCZrS"
    b"kN4l86rVb4wIK1k5/vyr8aH2A+k/0MgsZh3uxq1YjcuEFAV+x37h6e4UhuuezPZroSksxzM6"
    b"T1GmsVlydkHQiCJ+loQdEILmI7gBy4QcakBYdW7Eo3jV39ObY5iUf4TMi9X4vCTkfazXWZBs"
    b"YAN2lHh2Y1VWpRWYEFLvIi+6JwPnmBSvjgsPpad4WMpYt2FJRu5hvB65TwufBz3BhOTEc70y"
    b"gq3Rxil5k1KEcftbNPBsbvJzoHBmVpiPWdCQJva2XKRt4A3peydLpr1Zmtg558R8GJYWgKfr"
    b"kjWlOHFvXbIuMB5tH1XzIW6R4sRC4YOoYVMdkiLt6Pm6XoGJqGFvtwTrpLSj76lDCQ0cilqu"
    b"bdXp/AqC0di+JdSsFgpn8Hb8PdqqU5Ujt8R2Ry5FNbA9tre16lDlyNWxnc6lpgZmYttVcDwm"
    b"jMtl2eR0jxFpGe4YJ+PNVSXMfmFI0HKiVYeqofWfQpUjs7Ft9kPIPChKUbOtOlQ5ciC2Kyr6"
    b"9AtXxPbHVh2qHPkittflUlMDRSD8slWHKkemYntHNjnd487YdrXJs1ZYKQ5a2BRlAIejljXd"
    b"khT7FRsyieoG90cNtYp5xUfVQqYpH0UNk3VIhqUIP5ZBVKcoUvgjMnydTkqbPP0sbTbxXbT9"
    b"VA7ChlABnBPqTv3Cm9HmJzJu810plYO25iKtwEtS1TFbOajAeqlA10tnXpQKdK22qWtjYzQw"
    b"J9Sdcs6ZpjScTgmnIXqKcWmY7ZOnrDkhTexf9fBNnI1V0o7rnFCymdBZBjAgBLsiThQTe2VW"
    b"pW1gkVABPFoScgiv4THcJGzuDMZrOW7G40Lp9XDpviPCEtuLQwhtY4lQPCufJ2n32iPEqdrB"
    b"Lud5LUK6PSqc2boKl0sLwix+EPbtPxbOas2cg6Mr/AVMUjVunZJoRgAAAABJRU5ErkJggg=="
)

icons8_console_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAB"
    b"ZklEQVRoge2ZQUoDQRBFXzS4iIKCEoILA15Br+LZ1Ft4A0UlCyEuxGBUBPealTsXaRdd0UEM"
    b"2tPlTE2oBwUNSVf+o6fTMwk4zr+xBhwBEyA0rCaSfRXg2ECg3DqksBJ78xfNLPvE7K8tGQC0"
    b"6suTRQBYqjuFFi5ijeIeaTQLsyLtwti/tSzgItZwEWu4CLAsZYbZPX0qZ8A9sKuaJp3P/GVF"
    b"TmTeM9BXi5VOtkgHOKV+mWwRiM/K5zL/AdhWiZaGigjAOnAlPcZALztaGmoiABvAUPrcAFuZ"
    b"/VJQFQHoAiPpNSTKVUEAguaBOAXeZdyRqhSNFekSL6kA3FHtple7tHrArfQY0dDNvgM8yvxr"
    b"qt3kM7JF+sATX5t7Uy1aGlkiK8TTPAAD4lny/fVxoXdKXZQRaf/6tp+ZAi8S9gB4m/MBZSg1"
    b"z3/7tYaLWMNFrOEi1nARayyMyEL99XZZdwgFUu+YHeevfADs2tPOHBgeRwAAAABJRU5ErkJg"
    b"gg=="
)

icons8_text_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAA"
    b"3UlEQVRoge2ZWwqDMBBFr6WLq922O6nuo/0xICGayftS74EggsnkYDIfM4AQQvwjbwAbgG/n"
    b"sQKYa4qMkHDjU1PELdobc9xH4410I1dkge1YLIVzzEzG79zvnbz3lBglc6L7fCYsfhUwxNnG"
    b"c+ZEud0d2fbnMYtUTYu94sz7gsfc/orM8VOnJZXmxGlOjkg2t7sj9EiEDYmwIRE2JMKGRNiQ"
    b"CBsSYUMibEiEDYkE8HsoZzTrfdQi1EOJFbFbFPmKSa1bVa1z6Y4E8Ou2sQGQHi2/bmvpDQ6v"
    b"6wohxBh+1Qai3Sp+mhwAAAAASUVORK5CYII="
)

icons8_info_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAD"
    b"7ElEQVRoge3ay29XRRQH8E/1Z/sjoNCWAkuJT9RU9gQfGy3BBZpoouIOgxseQbfq0ro1aeI/"
    b"YogYRRCNVUTdWAvoRmuiCTa+KgTNdTFzM7e1r9+98/sVEr7JzUlm5p7HnTlnzpy53MC1hb6M"
    b"vIbwEHbhPtyBLVgf+//Cz/ge3+AMTmM2ow610cYLOIF/UXT4/IN3sR8DPdYdrMPL+Kmi1GV8"
    b"gFexDzswiFviMxjb9uE1nIzvlO/P4JjwcXqCvfiuosDnOICNNXhtwos4W+F3EXuyaLoE2ni7"
    b"IvALPJaR/xi+rPCf0IXZ2SYoXghOewg35xYSeR7BnDTbW3Mx3y5Md4EpPJCL8TIYxXSUeSHq"
    b"0AgjFYafYXNThh1gUAjRheCT2+oyakvL6RNpP+gl1uNTaZnV8pnSsaeEza5T9ONNIUTPYDy2"
    b"dYphaVVMdPryXsmx6/rEuP9vgOM1eY1KAWBstS+tk/aJQzUFE2ZhoSEzDfgdlZx/VUvsFWmf"
    b"aBJicxvSwleRz9GVBreltKPpZrfY0nqjIc89kc+PVsjN9ksRoin6BWNmNHP2KvqkSPrccgPf"
    b"i4MONBTYTRwUdDy+1IAhIa2+rF4C2CsM4gququh5U2XAw4Jzf4zfeqpaZ5gVNsmWcJDDfEN2"
    b"Rfph73SqjZOR7i4bWpXOHZF+nUFQsUR7rqN1qeO9ZUN1Ru6K9EImYd3E+UjvXqzzkvAl6+RV"
    b"S2HhPpILmyO/XxbrvBI7m8b6KrplyIBUJ8D8pXVdo2rIn5FuWAtFOsRtkf5eNlQNuRRptjNy"
    b"F7El0l/LhqohZbRaNBJcY7gn0jJ6zTNkKtIHe6ZOfYxG+m3ZUDXkTKSP9EqbBng00tOLdQ5K"
    b"SeOmTAK7EX6HpKSxdPp5MzKL94UY/XQmod3AM8Jed0Ilai3E88KXO5tJaO4Z6cO5yOvZ5QYO"
    b"CMfIAo9nEJzbkCcinx+s4hriWBx8TvP6bk5DWkLWW+Dwal5oS7XeIzWFrnTBUwflB57WwaVQ"
    b"Wa2Yk2J2J8htyE78rWZ1Z0L6AsM1hOfCiJB1FHirDoO2UBYqhDPyWhSxN2Ay6jCpwT3jiJAG"
    b"lNcKIzm0WyWGhEJIeR3XOJndLk3ttN7kYjsrMs/j9lyMt0rLbE6ovbaWfaMeWkJ0Kh17UkrZ"
    b"s6EtBYBCKCjnun3tE64yyn2idOyu3r2PSdNeVu0PCklnpxjCS1LaUS6lnLfFy6ItLK8ynSmE"
    b"jPQUXseTuF8I2/3xGRYujZ6KY05JBY8y7Thsjf6AGBCq4seFI8BKG+HC5yreERLARgbk/Klm"
    b"o1CL3S1ULe8UwvWtsf8PoQ51UQjpHwmzsmQqfgPXM/4DBaQ+gHlAM7wAAAAASUVORK5CYII="
)

icons8_laser_beam_hazard_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAD"
    b"tklEQVRoge3ZT2hdRRTH8U9erEltqjFtasVKg1i1GEQSja1VidQuRFCx+Kc0CCpmY6UWq6iI"
    b"IqKNGmiLLYhQXUjRTV0ItouCiEihLvwDQguCqFijdVNcCF3pYs7z3b7c/LkvuUmE94VL5s09"
    b"c+Y3c8+cmXtDkyZNmjSZB1pK9n8B7ovyx/i7rI7KHEgLPsNf8XspNuKfEvssha04jkpcx6Pu"
    b"f8US/IL16IprfdQtmUddhXkFB6P8OnZF+WDcm3XKWCOr8A36sRzXSqF1AqfwLW7AzyX0Pat8"
    b"hJekSdqjtkb2Rt3L+HDe1E2T7DrYglvr7j2Exfip7t6CooKv1MTuyrF5S22QX0ebBcejOCaF"
    b"z7NYnWOzCjvD5gs8MmfqpslS/IoBXIZnJrF9ThpkH37DhaWrK8AI3ovyGybfK7Jh9778EJwX"
    b"rsCfuBTrpPifiq24BZdE2zWlqSvAIbwgxX01xWZZhw11dVXbSrQ9VLLGKbkdP6IdD0trpJ7B"
    b"uOrpxxDOxw/YVIrCadAq7dKb0WF8rFcHNag2kBvrbEai7ebw1dqomJnk8cdwRgqLbdgnxX5n"
    b"3G+p81/J/O4M27fxZPg4Ez7nlIswhuvRg6czAvfF3x4Mqz2R4ajL2oi2PeFrLHzPGaN4N8pv"
    b"Sim1Sif2S/vEYSl8RqLcF/c6M/aLpR1f+BwtTXUda3AaK3AbHoj6fmld9EiCD0hJoEp71PWF"
    b"zUC0gfvD14rwPSfp+BPpmFGRTrfZdNsihdBhtOW0bcORsKlvVz0p74w+ClH0fWSTFBq90mL9"
    b"Dn9gbZ3dRjw/gY9RaROspxef4wN8jydwdLrCimSt87BbmrF2XCmdYIvSgotzrlPSRLVHH7uj"
    b"z1knO0PDWJljUzF5aLWrhVbeJK7Ei1E+Gn3OKl34XXr8EzEgbXjVk+0B5w6mTW2xrw7bvJPA"
    b"U9LT7o0+u2ao/Rz2SmsDXp3Ctmj6radNLQXvj75nhbXSgl4mzeI9k9g2siHmca+UMJbJTyYN"
    b"cQTbpXNQXihkGcoIvElaB4NxVaJO2AxN4WtP9Lk9NMyIu6TPOIvQjasKtM07NE41EVmuw+PR"
    b"94nQ0hCLcBJ3NuogGJR/jJ8Or0nhdYd01M/LhFOyA582KCDLBuNfrKZLt/SNTGjZUdTBcunM"
    b"c02DAmaTbbha0nJa0jaOiXbOLVK6PImbcXcJAovQjS8lTQ+qbQX/MdFAxqRvUB3St6pjJQks"
    b"QgcuV/BA2Sq9G5yV/jGzEK6zeMcMXoebNGnSpEmTifgXBxu98dH6sbAAAAAASUVORK5CYII="
)

icons8_about_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAE"
    b"cElEQVRogd3aaahVVRQH8N+7ms/qORSvjMih8EkWFWI2SoVlUERBaBEFCpFgZUESBRVaRBF9"
    b"qQ8OfcuywqCiAQoqo5kmQiuTnLCQcMjZetXT24e1r+e+x5vuved6n/3hsM85d5+1/vvsfdaw"
    b"1+V/gqac5AzBZFyMc3EGxqEFw1KffdiLzdiAVfgS3+PfnHhUhWbMxApBsljlsRvLcQMGV0um"
    b"mhlpxb24A6PSvSJ+wBf4DuuxUQxwX+ozDMPFbI3HBbgEZ5XJ/g1LsEjMXl1wLB7GHtnb/Abz"
    b"cFoNcsdhvngRJbnbcLcaZqgnXIq1ZYrewkV5K8E0fFim52ucnYfgJjyIjiR4FabmIbgPXCsM"
    b"QhF/YXYtwo7BS0lYBx5N944Ujsdi2ew8rYpvulksnyJ24ZocCVaK2WhPXBarYDBNeDU9uBXn"
    b"1YFcpbgKBwSnp/r70GPpgZ1y+tBywpX4W3Cb1VfnK3AQ/6QHBxpuFwM5gLaeOh2HTanjIzkp"
    b"PkmELpPTeR5YJjh+qofv5aHU4Vv5OaJyq7MoJ5kjsSXJvLnrjyfIPPblOSkkwo3SQJbkKLe0"
    b"xNZhEBTSD7NEHPQ+Ps5RYbGH81rxvBjEeOE8D2NNUnR9jsro/I205iz7PsH5ndKNCenGdmma"
    b"jhK0ioijHS0Fmdd+T5jeowU78JWIQqYVxLTDJw2jVD1WpnZKQea9f6yDorkiQtiJBXWQX+J8"
    b"9mCcmi421UHRKGHa4ZQ6yN+Q2jEFjEgXe+qgqN7YndoRBZkX72gQmVrQntqhBZ03B442lFbT"
    b"3oIwY3Byg8jUgpKT3VXAz+liIOUe/UWJ89qC2FCAKQ0iUwsmpfanAj5IF43My6vF1aldWRD7"
    b"r3+IPdsJDaNUOS7EGJGbrC4Is7ss/Xhno1hVgbmpXa4sRWgTA9orX+u1UH0SqzFi4+6g2Es+"
    b"nFitw4vClyzMUWG98DiG4hWxWd4Jo7FfzExe26IL5D8j03FIzMjYnjrNTUo3yYK9WjAWc9Ix"
    b"qY++/UErfhUcH+itYxPeTh0/EknLQEGzyJmK+Ew/stnhIs4v4jVRVms0huB1wWmzClKC0aLq"
    b"VBQpcCMDyhbZKtmBcyoVMFo4yiLuypVa/zFeVsnaJpx2xWgTdrpDbaW1atAkDESpyLoWZ1Yr"
    b"bIUu+0ZHCNNFbbJktpeJ5VUVbk1C2h2Z8L4Zt4i4rzSAzbiuFqHTZRWiXm11Nzixgr6n4za8"
    b"LHLv8orufOG5+42u2/IzRajSjKWywKw3tIi3OQfnC8uyRoQO+0Utg6gJjhSxUZvOZYZSqfu5"
    b"NLB2VaJJxFiHktBnZXFYdyjgMhF2lNfd/yw77+vYijdwj15CjUoGMFhUb28SFup+PNNN30GJ"
    b"/AzcKHNKRbHjtxRvihmaKJbOCJkPOiCs0MZ0bKmVfFc8IStBzyi7P0Kkv/NEcXSbzm90PZ40"
    b"gJKxz2XkOgTh7bpfDr+IgecRAOaOqXhXhMXlpA9gNV4Qf6CZ2CiC/UG51RoiLMtwUdX9vSGM"
    b"qsR/ME41xQZApAYAAAAASUVORK5CYII="
)

icons8_align_bottom_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAA"
    b"oUlEQVRoge3ZTQ6CMBQA4afx/ldygZ4Ldi4MSX9oH5NmvoSVUjtAgNgI6RbviNg7ty1zoo/C"
    b"5/vk8Yd5VX6vdUJXD0CzZ/YPzmIIjSE0htBkh3xj0ptC7ZO994H4v9+0NwUvLRpDaAyhMYTG"
    b"EBpDaAyhMYTGEBpDaAyhMYTGEJplQmoXQ9MXN1uVzsjnwthn/56PHk9Yo9cvsv3mv8xdSzQH"
    b"L7opUXxgNIwAAAAASUVORK5CYII="
)


icons8_align_top_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAA"
    b"qElEQVRoge3aTQqDMBQA4Vi8/5HcWM+lC7GL4B95Eqc6H3TRheENbVLQpiSWJns/3jJFud/8"
    b"nzun0Jt1ad43Ja9+Zb0hsN53b9B8s+eim//qw2Rz3ja6wIbqp99jTi1DaAyhMYTGEBpDaAyh"
    b"MYTGEBpDaAyhMYTGEBpDaGqHDIFrd+/GH1lu6de6rphfLRpDaAyheUzI2Yeh+L92HH0ikV/T"
    b"tefs0r+ZAAn6K06SZpqKAAAAAElFTkSuQmCC"
)

icons8_align_right_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAAAXNSR0IArs4c6QAAAARnQU1B"
    b"AACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAAGYktHRAD/AP8A/6C9p5MAAACgSURB"
    b"VGhD7dfLCoAgEIVh6/0fKip6rS4ys0hcWAs92f/BMAgRHkxoAoDUbhWN1j+PIGreBlnO8m+0"
    b"Zs1nZQ3Wn7pe2orv2fcQ19wRNQRRQxA1BFFDEDUEUfP7IJv12lbrXfEZJeKOqOk2SKtZvLSK"
    b"Z/brYXXZmT3lyRWle7utuexqCKKGIGoIooYgaroJ0s1PY3oik3VVzOyfQRDgF0I4AEuCXBYR"
    b"wmDyAAAAAElFTkSuQmCC"
)

icons8_align_left_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAAAXNSR0IArs4c6QAAAARnQU1B"
    b"AACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAAGYktHRAD/AP8A/6C9p5MAAACvSURB"
    b"VGhD7dnRCoMwDIXhbu//TsKcvpZrIBnDiuhAPa3/ByHUC+lBAi0m4HiTV5We3qtHEDVrQd65"
    b"Ym7OrD7Xbg/vxl5i4lmsr/C7r02YETUEUUMQNQRRQxA1BFFziyCj97MN3v8W94EqMSNqbhHE"
    b"7s4xN4r1yvWlemffavFuH0nDfK2k2BvDroYgagiihiBqCKKmmSDNHBrXvkjnXZX9GlxUnChr"
    b"wrCraSYIcIiUPoSrXBiRr7O2AAAAAElFTkSuQmCC"
)

icons8_circle_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAD"
    b"l0lEQVRoge2az0tVQRTHP6l5BU18Wgq1SOiXukjdFVhtQhGKWliE7toX4n/hDypJWmZ/gRkk"
    b"/SCCqEVIKBjlr2ihtagMNAnqKb0Wc6/de+687o9352nhFwbu9Z5z5nucMzNnzhvYxtbCjgRt"
    b"pYCTQAvQABwAqoFS+/t34BPwHngLvACeAcsJcogNC+gCHgLrQCZiWwceAJ22rbyjBOgBPoYg"
    b"G7Z9ALpt23lBO/AuQQdkmwfaTDpQAtwKIDEBDAAdwFHUvNlpt5T9tw5bZjLA1hAGwq0GeJWl"
    b"wxWgFzgSw24d0Gfb0NkeRy0YiaAWNdyykzTQD1Qk0EcKNUppTT9zNoecUIPeiTeoMEkajail"
    b"WedM7JEpQR9OI/zZG0ygFLir6XecmHNGN7FvA4UJkA1CITCs6f9mVEPtGiMj5McJB4XAqIZH"
    b"a1gDFjArlGeBXUkzDYFS/HNmnpCbZo9QTGNmYodFE7AmOF0NUrLwpx195jiGxjW8nBYJmPhd"
    b"QmGFZPaJXFEJfMPL7dLfFB4J4V7DBKNgAC+3sWyCKfypeJy0wxQa8HJbA8p1gueF4ESeCEbB"
    b"FF6OZ50PBS6hFqH01DyvyHgi3k84D25H6oTQS2N04kNyqnce3I4cFkKzxujEh+R0SCe0hDf+"
    b"Kg2TioPdeDl+0Qn9FELF+WIXARZejj+cDwXZNP41uB1ZFd82I0kMguS0wdntyFchtNcYnfjY"
    b"J96XnAe3I/NCaCvt6g4kpw3ObkemhdAxY3Ti47h4l5wBOId3RZg0TCoOXuPleEYnVIE/aZS7"
    b"/WZCJo1pXEmjO7SW8ecyl02ziwDJ5THqjKJFJ/6DVcoYtfCoQi21oQ9WFqoq7lYYMMsxFG7g"
    b"5bRAiMyjG38sNprjGIhm/MWHK2EULWBGKG6lctAcESqObUI5gypj5rNAVwTcExx+AaejGhrC"
    b"78ww+XGmCLij6X8wjjELVTiWxkaBsty5ZkUZ/pHIoE6HsY8W1aiYlEanURXApNGMf346c3RP"
    b"rsZr0TuzhqoAJnGSrEItsXJ1cpzYn0AfgBoZXZhlULtrPyqFiIoG1D4lNzt3OOU8EhIW6vcJ"
    b"XYdOm0KN0gXU3lOJiuti1H+9CbgIXMefAMrVaRDDx+1W9KGWVJshxhIbFxaqtL+YoAMLqB17"
    b"U25AFKOStzH0EzWorQH3bRs5hVGSl2rKgVOoMmY9cBA1UZ3UZhX4jLo1MQ08R12qkUWPbfwX"
    b"+A3NNtEphGbglwAAAABJRU5ErkJggg=="
)

icons8_flip_horizontal_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAB"
    b"+klEQVRoge2aO0sDQRCAv0Sw8IEIIiIERBAsREEQRFLaWtra+APEytbS1tLW0tZSBEULRUEQ"
    b"EURLFUREIuIDTWKxGbwcm3CPvds9uA+uSMjNzgd3l5nZg5ycnKzTCSwDN8CB3VSi0QksAXdA"
    b"3XNkhm5gBbinWSAzIj0ogUf0As6L9AJrwAvtBZwVGQDWgVeCCTgnMogSqBBOwBmRErAJfBBN"
    b"wLrICErgk3gC1kRGgS3gJ0KyTohMANvAr2GB1ESmGgLVhAQSF5kDdoFawgKJiZQbAmkkn4hI"
    b"Gdi3IGBMZB44sSgQS6QILADnDghEEikCi8C1A4nHEjlwIOFQIsUW33+FNU+JI9sJ5MShAJxi"
    b"/17QHS0vLd09UkeVGy5SDnuC7vH7hOqtu4ymFpxIj19B/hDPPIGeUa1qn4HkwhBLxIu/RKkA"
    b"G0C/ieABMCYi+IvGN1QrO2RyEQ3GRQR/Gf+OEhpOYjESFBH8jdUXqlcvGV4ncRFhkuZW97vx"
    b"ecxQ/NREBP/woQrsAOMx46YuIvjHQVXUJTgdMZ41EWGE5gFdDSU0EzKOdRFBNzLdA2YDnu+M"
    b"iKAbYh+jKoh2OCci6LYV2gk5KyLoNnouUEVrwfM750UE3dbbJWpDtIMMiQjdwCrwwH/yV2RQ"
    b"RJDt6VsCTFGygPeFgUPLueTkZJY/7wYg/LWeLJAAAAAASUVORK5CYII="
)

icons8_flip_vertical_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAC"
    b"j0lEQVRoge2ZTYhNURzAf+Qj8pFEKESJEqUoSaIUZaEUK1asWIiFWIgSC7EQC7EQpShFiYWP"
    b"1TRDSlKTj5WSml7SJJPJMPO3OP/xnut+nHPuOfc9dX81Ne/e/zn393t3mundgZqampoSjAOe"
    b"Ad0txx4DPXruv2EPIPo1yujr3W0x8mAs0Et2yFud6Xh20ZROCxFgZxu8nBgDvKY4pJcOvyvb"
    b"MaKfyA8Rne1YXmAkD1Ic8hJzBzuOrRjBBjCZ4hABtlTsaEUXRu6IvrYJ6alS0IZNGLEvwFQ9"
    b"ZhMiwMbKLC14ipE63nLMNuRJRY6FrMUIfQVmtBy3DRFgfSWmBTzEyJxKHHcJeRBfM59VwAgw"
    b"AMxKnHMJEWBNbNk87qnE2ZRzriF3o5rmsBwYBgaBuSnnXUNGgJURfTO5rQIXMs67hghwK5Zs"
    b"Fsswd2MIWJAx4xMyjLnTlXFDL3w5Z8YnRIDrEXxTWQz8xNyNRTlzviG/gCXBrVO4qhe8VjDn"
    b"GyLAlbDK/zIf+IF515YWzJYJGQIWhhRPckkvdNNitkyIABeDWSeYA3zH/L5fYTFfNmQQmBfI"
    b"/S/O6wXuWM6XDRHgXAjxVmYC33Tz1ZZrQoQMALPL6zc5oxvfd1gTIkSA0yXd/zAd6NdN1zms"
    b"CxWS/JzjzUnd8JHjulAhApzwtlemYT6HC7DBcW3IkH7MT4Y3x3Sj7qLBFEKGCHDUqwDzbKqh"
    b"m2z2WB865DMwxcODw7rBc5/FhA8R4JCrxESaz2+3+XVECekDJrlIHNCFr/B/PhsjRID9tgLj"
    b"gQ+6aIdnRMyQj8AEG4F9uuAN5f6HEStEgL02Au8DXzRGyLukdNo73rCptaSr5Xufv0VZ9AXc"
    b"q6ampqYN/Ab7PEdZ7CnXLgAAAABJRU5ErkJggg=="
)

icons8_oval_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAD"
    b"TElEQVRoge3ZzW8VVRzG8Q+3yltLWxcI9YWYGDHGEIFYMNGFVTdojBr1L3ADSohB3BsCuFJ3"
    b"KqjhD0DRDejK+FaQutFECyTiQqoLSbA0JpbwUhdnGm/PzNw7vS9zr/F+k7OYM79zfs+9M+dl"
    b"nkOPHj16/JdY0qJ+bsdWbMI9uC2pW4bhJGYas5hKyiS+x7fJdcfYirdwGnNNltN4E1vKEt+P"
    b"l3C2BeLzyhm8iJXt+AFL8TIutPEHxOUCdiW561JkjDyED7C+RswV4V3/Tnjvf8Gv+EsYG4Sx"
    b"MoB1uBMbMYoHcEONvs/iBYwX0JpJHw7gmux/bBYf4VmsajRJ0vY5HMXlnFzXEi19i+18CJ/l"
    b"dHoJ+7C2CfF5jGB/kiMr93EMFu1sGKcyOrmOt7G6hcLzWI13kpyxjpPCH12TZfgmo/F5jLVF"
    b"cm0eTnLHer5WZxI4nNFoHGvap7Uua3EiQ9d7eQ2eyQj+XFg7Os0AvpDW91Qc2I/fo6AfLWJg"
    b"lcCQsK2p1vibaOF8NQr4W9gzdRv3CtN+tdZX5m/2ST+N10qXWJy90hNRBR6LbvypwPTWQYal"
    b"15lHKtgWBR5JAruVaXwY1W2rCPudao6Xo6cpjkXXo4SRX/2Y1pUsqhHusFDzFGGGqq5c3iFx"
    b"i2G5aJatdFZPw8S6r1dwMars5HakKLHGixWciyo3lySmGWKN5yqYiCofL0lMMzwRXU/AoxYO"
    b"nGndvSDeJL0gjhG2KPEUvLczGguxT84WBfZEN2eFDVq3sUH6u353dUC/9FOZ1F2v2LDgecUL"
    b"Ycr/ejoKmhM+ZgZKElqLVfhKWt+TeQ3ezwg+qT2OSVFGBM8s1vVurUZLhQ/7uNGUzpgPY7LN"
    b"hy8VcCCHhKeQZQcdxM1tkbyQNTgk2w4at4ixO4hPMzqZw4zg+o20UPg8t+D1JEdW7mMacDXr"
    b"WaaX8bFgdzZjUgzieXwi3zK9qo5lWsTEflAwse+uEXNV2CZM4Af8LLzbM0mZFzwoHADdhfuE"
    b"85BRtU3sM4KJfaKA1rrcKFj8ZR4r/IGdSe6WsxI7tOaUKq9MYrs2HfRkMYo3pE2zRspPSV/3"
    b"NyqmVYeht8o+DF3h34lgRvisPm/hYegpYXvUo0ePHv8j/gFzYrbzMmFdVAAAAABJRU5ErkJg"
    b"gg=="
)

icons8_place_marker_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAF"
    b"XElEQVRogcWaW2wWRRTHf1/hq4iNtJi0pSXBIhob610LmBoUiNJ6CYYoXtDok8YYwUuioklF"
    b"H3wg+OSLGhOjqFhNCSJq8BJFqtUnEZSId0wVKMYGsFR6WR/Omex2O7Pd3c4H/2Sz7ZyZ/5y5"
    b"7DlnznwF/KMBWApcDtQB9VreA/wJbAM2Ab+WoG8vWAh8CQSx55g+8fIvgCtPiKYO1ABbCBX8"
    b"FlgDzFVZQZ8aYB7wFLAzUv9doPq4ax3DecgWCYDdwI2I0mmwGNihbf8ALi6FgmlwAXBYFXke"
    b"KObgKAdeVI5DwPnetEuJGuB3VeBRD3yPKddvHOdtZr6JFzxympV5xyNnIhZqh9+Rbzu5UI58"
    b"ZwFwhUdeJ4yJvT6hThWwGugG9uvTjWyhyoR2Nyh3lxdNEzCb0MS60Ab8zVi/YZ6DQGtC+11a"
    b"7/SJq+vGKu1kjUPeBgxpndeAZmTLlCN+5Q2VDQFLHBxPa52V3rS2oFM7mWeRVRGuxL0JHPdp"
    b"nV5gmkV+mcrfnpCm4+Ar7cRmIlcTrsR42IDbdNeorDunjqmwF4mbyiwyYwTmpuCZj/ujLtM+"
    b"9ubUMRX2AQMOWS8wQjqTXK51DzjkA0iknBq2mU1CH3ASMMUiC/SdJtYydQKLbKr20ZdFsawD"
    b"OajvGRbZz4iCF6bguUjr/mSRmfNLbxbFsg5kt76bLDITWqxKwfNArE0U5+r7+wx6ZcZKZDs8"
    b"YZFVIisWICbWhftJNr/GjySZ8AmjWTv52CFvJXSIGxB/YxzifKCD0CFe7eDo0jolDeknIR/h"
    b"UeBkR50lyGy7QpRe3IM4FRhEYrO0B7TcMN59aUKdacAjyLl8nz5dWmbbTga3KvcrXjQdB7do"
    b"Z6+XgHuTcl9XAu4xqAD+RY65SbObFdWIIzS+KhOyml+AI8CbyIDuzNHehbuRAbwM/OeRNxFN"
    b"yBb4kXyTEUcRyaSMAGd54MuEz5DBtHngulm5Nnvgyoxl2vn7Hri2K9dVHrgyYzKSEhohXXzl"
    b"wgLCZEbJfYcL9xCmPfPiU+VY7kOhvCgiH3yAzGxWtBEmM3wYjQnBeOPPM7YrAF9r22t8K5UH"
    b"ZcA3ZLdgy7XN9lIolRetiFJ7sJ8e46gg9BstJdTLigLQCNwFPAtsRTId5kRn4qT2FFxrte56"
    b"/X8mkqHZCqzTPhrxaMUqgRXAW0iiIB6SDxHeazQA/UiIPyeBswnJkhxCruYALgGGLfwHtO/b"
    b"SE61OtEMvIoEcXHijcisLwNmxdq1a70PHLwFwojg4ZhslnK2ax/xiRtQnZrTDOAMJTGNh5HL"
    b"yweRpR4PUwjN8U0W+R0q20m6tFGj9r2N0SvWqbpasQQJoQMkwl2LJK2zYoF22gNMj5RXIye/"
    b"IdIl8eKYrTodUR37sOSPm5C9bUZbF6+QEc8pV0ekzKz0ugly1xOeUo8C50SFHxHeBfqwFBWE"
    b"l6S3I+cWE/ZP9cBfQHQNgA+jgn4tnG5plBctyDbq02cQexY/L05DdO6PFprZW+SxI5B7FPOB"
    b"PumZe7Hy/hItfFwL/8Gvp52MRMab9W9faEF0DZDrjFEdmpvaYeAl7PndE406RDdjirdgmaAi"
    b"8Axy8A8Q79sJXIvf29usKKoOnYS/aRlAdE3Uaw4SFgwS7u/DyOgfQjzrKaXSWrmbEc//HuGv"
    b"KwLVqQNLCJRkamuROGsFY/OwI4iB2IWY1B4km9iDhBaDyB4m8q6KvIuIg5yJXLXVA2ci/qyB"
    b"sYesHUiAuV77GYO0PqMW+aHAIuBS4GxKt92OAT8gh65PkIT5/vEa5XV+RST/1ISEDrWIcZiB"
    b"zPAkRq8AjF6hYVXur8hjVngPsqKZ8D/iZ4huqztQ5AAAAABJRU5ErkJggg=="
)

icons8_polygon_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAC"
    b"/0lEQVRogdXZT6gVZRjH8c+9edHECrWgugspCyJqJUirFv4Bb2FK0qJNLhRcikXoJhBdtYhA"
    b"JajlRTcuNHPhIoJAF+FKCgnh3sXtamVGKvgv/02L5xxmzumce+f80XnnBwOHeZ/3eX/fmTnv"
    b"zPu8DEfv4iIu4b0h5axEs8gax19Yj7FKHfWop3BIDlE8/sEk3sfiqgyW0TuYEabvNn7P4ADO"
    b"a4W6hW+xFcurMNtJS/G13OQ5rOoQ9xJ24gweFOLvN87txiuPwW9HfYDL8qu8G0+U6PccPsJJ"
    b"/Kv1bp3HXp0vxtA1ju8Kg/+AlX3mWiagjuOmVqhfcVA8orOYGMh1QSPYgWuNga5iW+P8MLRY"
    b"TAaTYnJonzB+G8Ygr+LHQtJjeGEYibtoTEzbVwpjXhwk4QJ8Kv4DGf7AlsE89qRNjTGb/5++"
    b"7v6bOCu/IkdVM10uwu8ND5vKdmp+XsyI90GGaax9BAZ70Z6Gl5/Kdih+XmT4Qhpv4qfF5JIp"
    b"eVGn5RBTj85XX9ovfH1fJnitHKTqx6ldz+KG8La6TIcmSIr6Ung7XiY4ZZBx3MFDvDFfcMog"
    b"8I3wNzlfYOogL+Oe+HKe84s5dRA4Ijx+NVdQHUBeF+uaO3ixW1AdQIhVZobPuwXUBWS18HlD"
    b"l2/AuoAQb/kMn3VqrBPIGuH1byxpb6wTCFG8yLCrvaFuIBvlK8iFxYa6gYzgF+H5klhToX4g"
    b"BEDT9+xoxWYGUbG2nBV/1OmOfKi1ZLSh2VAnkJW4Lvxub2+sC8iYKEY0Kzz/U11AmqvFaTzT"
    b"KaAOIBNilXgXb3ULSh1kXF5K/WSuwJRBRkX1P8Mp85RQUwbZK7z9iefnC04V5G2xTn+AdWU6"
    b"pAiyTL5Hua9sp9RARnBCeDottjpKKTWQj+Vb3Ct66ZgSyCr5hunmXjunArIEF4SXA/0kSAXk"
    b"sPDxM57sJ0EKINvlpZ7X+klQ3B9ZMzxfPY0/VfCwtd9ExSRVH1f6hRjVVoWoWLcH6TwhNkSn"
    b"VLP11ny0Wpasveo/T0QoE45QIQcAAAAASUVORK5CYII="
)

icons8_polyline_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAD"
    b"E0lEQVRogd2azW+MQRzHP1tV4qA9IF4S4Wma6EGCiwtOxEtLpE2chCxWRYtGw9FFwhEXf4Aj"
    b"J3rYNOEiIqFJaR3EQV1FSF+U7tq+OMzT9Jl55tl9dsx0uj7J5Nlndp/f7/vdZ+b37EwLtUc7"
    b"8BaYCo9tfuWY0Q7Ma9pJn6JMGERv5I1PUSb8Qm9kss6nKgNGE/o/ZSwmCYCDQD0wAHy2GBtg"
    b"K/ABWKv0zwPHbSXJAtMs3uo/QM5WcCCD+HKiw6kEvAKO2EoSIJuIJgos5chp4tv8ogDo0iRZ"
    b"aL+BfuAM0GgYfwswpsR9jrhLVukh2Ui0zSCGwjVgc8rYGSCvxJlAzBfrBIg5kcbMQpsFXgLX"
    b"ge1lYi/JkIqSBQqapGnbEHAL2BnGC4BuxLcf/dwADoaUSiswpyQ+AdxGlM20pkaBoqbf2ZDS"
    b"MaQkPx95rwW4CbxGDK1q79rVJXEQckdJ/iThc+sQlayf9EOyy6Vwlf3Eh8PKCtesQTyZHxGf"
    b"E9F2wY1kPfXEa/6BKq4PEA9S1cQ05aubEx4rIu5WeX0OuZxPA2dtCkxLFtnIO4MYzcBlhKlt"
    b"1pRVyUbkMjxH+ie5MS7WI1+B4ch5BjjsII+Eq4VVXjk/6iiPc9QyPE7lMrwsWQH8QDazz2VC"
    b"V0NrFnih9DkdXi43H/6bebKJeBlu9SUmAC4iVnUtBtePIM+TInDOmroI5RYpWeAhsDo8LwE3"
    b"EMvVJsS2TKPm2BQeG4E9xKtVCdhB8h6VVZJ2Rmy1btuCkyb7IRbvhAuKtgMmGXH58CoQL83/"
    b"TH1Cfx6xfaO+P4NYf0+EbbzM6zFgL3APaAivLwCXgC/WHFRgPfEtngJw2iBWM3AFTz/Je5FN"
    b"fETs+NUc75GN9PmVY8ZuZBMlxGKp5niAbOSpXzlmNADfkI10eFVkSAeyie/AKq+KDHmGbOS+"
    b"XzlmbCD+7NjlVZEhfcgmRvzKMaMTsY0TNdLrVZEBncT/rjEPnPIpyoRh9GuGQZ+iTJhCb2TS"
    b"p6hqqUP8INSR1L9saUN/R475FGVKG+JfhX6Gx5oz8RfUZnMRWR+s4AAAAABJRU5ErkJggg=="
)

icons8_rectangular_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAB"
    b"U0lEQVRoge2ZPU7DQBBGHwi3lAS65ATIiQInyQEQKOIGiANAzoAiwVkQFEAD3CBUEVSEFiQo"
    b"lmI8sdeEyPaA5klb7NojvW/9U8yC4ziO4/yelZy1BNgHdoBn4AyY1OiURwcYAi3gFjgH3mMF"
    b"CXANfIoxA9JKNeP0vh2k0xXBtZBDVWB5DKX4qgrSL9seQ+zKiQ7yUqPIskzlRH/sbeARWFfr"
    b"I+C+OqcoKXCs1mbANvAUK+ySfRdPq7BbkBFZpx//fGTRoBK1xRiQdZpDfyN/Fg9iDQ9iDQ9i"
    b"DQ9iDQ9iDQ9iDQ9iDQ9iDQ9ijbwg3ZJ5E5Q66XZQB3jAVjuoBxyptTdCO2hSVKTbLpbHiRTX"
    b"r9ZG4b7YY1NOdJC7GkWW5SZ2MSG07OUjfKXZY4WU+WOFS2BN3lR00LNH6HZPgTElPdYaaAMH"
    b"wBbhSVwAH00KOY7jOP+LL8rEkimh6HlnAAAAAElFTkSuQmCC"
)

icons8_type_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAA"
    b"m0lEQVRoge3ZTQ5AMBRF4cvqsP8VqH0wEBPx8yJt3XC+pDPhnURHTwKALxokJUlz5ZMk9TlD"
    b"3ojYzhgZsAmGzMHnSrmds60xRQ3RkKnoFNdSzpf1Wv/VN+5HFxkwekeeOLtXRb75uztijxA3"
    b"hLghxA0hbghxQ4gbQtwQ4oYQN4S4IcQNIW4IcUNIwNFOJeuuo5b9TiW86wCA71sAsWpmQWld"
    b"O0QAAAAASUVORK5CYII="
)

icons8_fantasy_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAE"
    b"70lEQVRogc3Za4hVVRQH8N/MpIVRoVZkDTUfggqLHn4ow6BQw0J6IPYCbUhTZ3ylidHLHtS3"
    b"oj5UUlAgRUlKlJEaFdHL6kNZJFlRaQ8ijfxQpviYuX3Y+3DO3HvPnfuc8Q+He+7ea++z/mev"
    b"vdba63BkYOZwK9AMHIu/MaaRSdqbo0tDmCmQuGa4FWkUH6KAt4ZbkXI4BUdVIXcm+gUiBzC6"
    b"3ge2yrRG4hvcqjKhbrRlxlw7yLzHYC5Oa1C/mvCS8KZ/wCx0FPW349co84LK5nUSHsAuvN0K"
    b"ZSvhfKnZFLAdN0ut4Eop0bE4qNS8zsaz2JeZ55Ih0L0EmzMKJNc2wVOtjf/vibIb4/9uXI43"
    b"0Vc0dtgcwuSowG4swM9Fih1GZ5Ttjm37M/378Xq878eEoVO9FF9EReZiRPzdGds2Z+RGC6ZV"
    b"wB+4T9gbj8e214ZM4xzcJN0jyf4YKazQ1UWyT2B27IdThf3Rh/Narukg6MCPApnB3Gsxnonj"
    b"Xmm2UrWiA1dgi6DQxzWM7ZKa2sVN16wKdAibfLXg97Ob+zuMw3S8j++xRrrhs3gyM25flLus"
    b"xbobIcSF5/CXUnf7IM6Nso8W9RewB5eWmfN6weUezshuxwqc3GwS47G1jHJbcWGR7COx7xDm"
    b"4Sy8Edv2CrlXOXRildTbJbnZOlylNGuoG+2YKmzKbBzYg6cEQg9JY8eNmbEdeDH2rcmZfxx6"
    b"8J6BL6sPH2FGs4hkMQaL8ZXSVTqMW8qMGR/7v860nYFlgoPIRvhDeBe9gnseEkzAT9K3NytH"
    b"7u4osyHTlqxSEuE3CNF/bIt0rYj7pSS6c2R6hPSjz0CvdEEce9AQp+3FuFdKYk6OTK9Aol8g"
    b"VHw+SvbEshbpOCgSU+kXvFM5LDSQxIlCUrkIR0eZ6XGeHao7cTYVy6UkFubIzJOSSGSWSffE"
    b"LtyFUfg2tg1pyWiFlMTiHJnF0gPX1kz7ttj2i5TQ7/gk3m9pjcqlSFaigE+Vrwcska7Ewfh7"
    b"uhDVC/hNMKEZgisudt8TW8oA8w10lQU8byCZLIkerI9yy6Vn9ocz8m1CipKNR6+2ksRtgmfq"
    b"x1JMwr8GkllaRIIQ3ZMguDfO0VVm/jZchy+FYFhOpmHMyZDoybRnyXymlAShVPqf9G1nT4vl"
    b"0CacZ2Y3Q/Es8kgkmCQ1szyZdVIiw1LIHowEwZwqkSAonxQnRubItAxzDU4iSTsquWFCnNiL"
    b"x5qpYDWolcQdVcy5Fuc0RbsqcbvaSCytct68w1SCTuWPwnUhuyfy0o4s0TwSx+GGGp+9Ssii"
    b"G0Y2L2p0JXrweQ3PbheOtzs1+OWgVhJLKsw1UaiiFOKYUVU8f5rUPU+rTuVSNIvEKLysNG/a"
    b"IRyeKiFJYwrxvmbMVxuJSi42Qa0r0iVUSvridUCN6UnWxVazsSuZUzF6hZQlD+2YIiSHSZVx"
    b"IzZJixfvCIG04kFrgdpWYlG1DCKOF4raxShXt+qLBC6K1yYDqyk745hOBnqCBULRmLASq3NI"
    b"PB3vlwg1q1rwjxAAW4bJaluJPJNrFO2Cd1ovNa1NUtM6EPumyXHHybfuFTkPGAoSxehSx2bf"
    b"LRA5oUxflkRvk5SsFjW73+T7xcqi9uEkQR0BcapU4ZXC97w7Db5vWo26UpQkfmSjbz0uttmo"
    b"K2mcjA/wp1AFn9JkpepBU9P4Ix7/A6+u1m3fs0SBAAAAAElFTkSuQmCC"
)


icons8_end_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAB"
    b"YElEQVRoge3ZPUvDUBiG4asqCCIiguAiFAQHwR8guDmKi+BfcHV0cHV1cHR1FFcHJ8HBwV1w"
    b"cRJxERFBEfFraIIZtLbmaJPDuaGEvsm5m4c0yckbEolEIpH4PzYx2OudCME7zjAX2Nnu8yfk"
    b"8jfsYDigsydBnrPlBRYCOTutByGXz+LU59HZxVhJZ6f1IBTlA1jDQ1a7xnJJZyf1IHwln8JR"
    b"Yd0exks629WD8J28gVXcZ+tvs+9lnD0JktPEYWG7A0z+0tnTIDkruMm2vdM6Oo0unZUIAhPY"
    b"L4w5xnQXzsoEyVnCVTbuEevo78BZuSAwqjUTyMefYOYHZyWD5CziMnM8YaONs9JBYATbeC34"
    b"ahkkZx7nbZy1CQJD2MJL2d/qC7VHdSP9tQpEcbLX/vIbxQ2x9lOUKCaNtZ/GN9X8wSqKR93a"
    b"Nx+iaAdF06CLpmUaRRM7itcK0bzoSSQSiUSiyAcoKiORfFCb+AAAAABJRU5ErkJggg=="
)

icons8_emergency_stop_button_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAA"
    b"CXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH5QICAg0Rhg4xqwAABFlJREFUaN7tmW2IVFUY"
    b"x38zrumOua6lI5ooGvjCJCnmh/yU+MX6UuELkUNpKpZQCiGUb2Ul9smXD4WEHyKQzbREJSTI"
    b"ME2NXlhnYWFWymXXZdSo1hTUXXdn+/JceHg4d+bOvXd0hfnDZc7c85znnOec5+08F2qooYYa"
    b"HiQkYuaXBGYB84EZwHhgtPR1AwWgDTgHtAADg21DZgF7gWuyuCDPVWCPjL3vyADHgGIFAtin"
    b"CBwFZt4P1aoDtgMbgaGmrw/4BcgBl4Ab8r4BmArMBuYJD427wMfAB8Kj6hgHnHXsbDOwQhZc"
    b"DqOAlcAFB58zQLraQkwGLpqJLwHLxdDDOIcs0G54XpS5qoKxQN5MeBBIxcB7OPCF4f2HnH6s"
    b"GGrUqQhsitl9J4DNxnGcdthSJOwwu7WpBO1DwAvAPuA88Kc8PwOfAs+UUcMtZq7tcbrYXsX4"
    b"QImTSAKtAVxuO/BSiZM5qGh7gOlxCHLMGHZ9GfotFcSQI+LBPHgLTgEdiu6bOCK21tnlAcY8"
    b"DHTJIl8HngOeBdbKu14jzE8y5kUZ5+EVY5OZKILsNXEi6aMKzzvsxA8TgW+NMHmgX/IxraY5"
    b"RbM7SgKoc6eVDpp5YtADwNwK+e9yqFq3oVml+gphveSTikmvidhpYL/sokfzSYX8xwP/lBGk"
    b"UVIXrz9UgvmGYnBO5VjrZUK7m/8GcAQeZhtj9hMEcdte/9pS6uOHGardrBLCs8DnwH+GfrQY"
    b"bBBMBZqA4+IJiyVom33WFBiH1U687eg/r/r75Pf7kPaYEhtb6ujbqOY5FOZERqr2DUf/BNVe"
    b"BLwM3BavVCluAb/7LFSffEOpe0VYDDN3iSZ5qnkdHwhzIjfN/cHiL9WeEmGhCyRGrBEnYNHg"
    b"s6bAgnQZ47TIqfbCCIJkgQ3AZ8Bbjv7HVftyGEHyxl1anFDtJcCYEEKkgWXq/3cOmjk+awoV"
    b"EO861Csl6uXRHA6Qg1kcUOOvGbvzXLoOiE+ENbKrislrDpoNjrtDwieKnzDv3jdj1znGrY4j"
    b"RbFJ4wWHKg6RYoFe0LuGpl6qKj3iJR8DvjJjfhBeVu1bFM2uONP4rE9VxbvL3zQeLGEWfVxi"
    b"jRaiVeoBFq8qmv6oaTxSPNM3u3ofYX4E3jTvPyxzsToJPOrgNwLoVHRfxxGQZopaeEybfHS1"
    b"zqhetkQFsiA24Xe/0ad4B5gWV3S1O7s5wJingd8c9arFUv7xwzYz5r0404Q6Y9RFuZuX8yJJ"
    b"Sb3/lnG/lvGSW80pnnI4gchIO6qMXwYs0D0ipaDrPsKPcHiyfMggG7hk2mYm7JBCQZCS6Rwj"
    b"eFK8U6dDiEnVrv+OlQqgNeCc3LEbA/BolGDX4uBzKsxJRPmssBV4x1Ex6RMjz4m77lbpxhTJ"
    b"255y6H4PsBP4SOLGPcV0KZ5F+dDTL3FiGoMAGblTXKlAgIKkHZk4FhD3x9CEZKjz5bQmKpu5"
    b"LnecNilgtDIIP4bWUEMNNdwb/A9jBMuJwvmIngAAAABJRU5ErkJggg=="
)

# ----------------------------------------------------------------------
icons8_group_objects_20 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAABmJLR0QA/wD/AP+gvaeTAAAA"
    b"0ElEQVQ4jcWUIRLCMBBFHwwOzxmKJRo8shrNAdBYqvHV9dwhvrVgexNEN9MtkzZNp8CfyXRn"
    b"tvvz/24S+BIKoJSVRtSlqq4AWEliC+wkvgDHkYSJqkMTaljgEaFw35ewwE12HYtEaiyeVuWA"
    b"kVj3VC/fZkZqAb9l6PZUYx2SvAz9EIs+hUNw9mogm4PwLN/KR/gzyyf8A3hOJXypOKe1GcRf"
    b"plzTDOATg/Znu3oLSZS0NyMj7nG4SlwBxmf5AGwiFHbgCHU/7pEK3fEKHqlJeAOCaiebx3Kk"
    b"lAAAAABJRU5ErkJggg=="
)


icons8_group_objects_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAA"
    b"pElEQVRoge2ZQQ6AIAwE0fj/L+NJDx5A1NbNMnMj4dDJhjakpQCEsFzOdfB+NLfrWYMLScNG"
    b"ZBu834v6N6ZNRO2xn9gkYiPSohatx92sxyaR0cd+8CapkIZhkwgiaiCiBiJqPJ0jX9CaRcOz"
    b"xiYRRNRARA0bkaftN/vv3mX6RHqkf5FtEkFEDUTUsBGJar/pA9MmEXaIatiIsENUgx2iGjYi"
    b"AEHsbs4PYp2OHEMAAAAASUVORK5CYII="
)

icons8_ungroup_objects_50 = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAA"
    b"rElEQVRoge2Z0Q6AIAgArfX/v2xPvTQrRSTEu7dWsOFJLEsJAGAmtpd7WRBTi3ruXRrojUMQ"
    b"87Sav7K0kZE9IiaMkRpyGtcXarnDGAlTiKTZrWgamhhRprvhMaJMad83WcKIAZelfLsuEsYI"
    b"hXiDQrxBId6Y4ThorTnCcZA3tI6DqvZx4Xk1ljCi8XYyyx3GSJhCehV7GZpxjIz61DUfmhj5"
    b"wPwfShgjAABzcQJJkRZZ1xWWJgAAAABJRU5ErkJggg=="
)

icons_centerize = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAAd0lEQVRo3u3a0QmAMAwFwETc"
    b"f+U4gSBSbRsuA5QeSXn5aEZERZPqAKmjSzdAQEBA9qpzk6zJUZBHh80MbG8EBAQEZOlA/DI0"
    b"czXIm0uV0QIBAQEBAQGxNP6/O82EpNECAQEBEYgrht1ISBotEBAQEJCbfGjx8ewCQdYKbRHZ"
    b"jdYAAAAASUVORK5CYII="
)


icons_evenspace_horiz = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAAeElEQVRo3u3aQQqAMAwEwI34"
    b"/y/rWVBREY0yey902BZSaHI8U67nrbXfS62o6yN7X+y5NqqrnWqrGSJJMvzlaIGAgICAgICA"
    b"NMz48HBXGrmhkXJHQEBAQEBAQEAMjV1z6gmgkYMpdwQEBAQEBAQEBKRNfvOpJtIsM9/aDGBS"
    b"7NmKAAAAAElFTkSuQmCC"
)

icons_evenspace_vert = PyEmbeddedImage(
    b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAAaElEQVRo3u3aMQrAIAwFUOP9"
    b"75zOUnCSqul7k5MkYPQPRhtlu0u8Fhc2MfTQWxFlGokqMwKFz1iuqN/1e5jsRgQA4PiMkrtr"
    b"EePFeDEeAPhvjM/F+0m/YrwYD59cv9vq96nGO2JG5vU/iNoMJLKY0+4AAAAASUVORK5CYII="
)

icons8_computer_support_50 = PyEmbeddedImage(
    b'iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAC'
    b'iUlEQVRoge3ZT28NURjH8U9VQtJa2mixJ3RnodJYYYE0kbbBzkJCuhPSF9ClxCsQUQsLkSAk'
    b'pDQEb0DEjpWKSIgWCa2UxTmTGdN7zRVtZyaZXzLJnec55znPd87fmUujRo0aNWq0stqJ25jH'
    b'r4pd8zG3HZ1AzFUg4aJrrgjmdix4C1uKqEvQFn/m2FbJcKoiRKI+aa+0VdJ1VdeyPNeVlMiK'
    b'qwGpmhqQqqkBqZoakKqpriB3FJxA6nJEgV1/c1YFpBfjeIhZLOIDpnEe24sCVAFkDO+1fxf5'
    b'iN1FQcoGmcBSzOExRoVj+xXp0X1PJ4HKBBkTIBZwOmO/JOT0DUOdBisLpFc6nLIQk9H2HQfa'
    b'1B3AtryxLJBx6XBKNBFtixhuU28PPgkLwB8qC2Q6tjsa7zfiR7SdalNnSPpqPp13lgUya/m3'
    b'gploG2lR/qAwZ5J8P+QLlAXyPba7IWO7EG2Xc2WHM+WT1exHPmBZIG9iu/0Z2+5o+yrAjAjD'
    b'bDHaL8Xyv/A2H/BTdPStZtYtdC22eyJj68IrrTfFyVjmeLx/kA94IzruWDuYbtyM7d5t4R8Q'
    b'htmMMIQmMr6nsd4ZeG5tP3cuSfeKbmlvzGOwAHpj5vfZWO8deuBLTSCyOivMlSUcS4zJMnfu'
    b'HwL9r4og9uEeTmKrsJr1C3PimfShXMhWOhwdCwLM5lVLP6gTiKJR8k6mJ7KaLKi4VsMpC3ET'
    b'U3gt7BuzuC9M7J6/PanDeNTB01hNiOTIMRXLV07duCrd4Pbn/HulENexfk2z61DrhCdc654g'
    b'PTPVGgJeCokeydlrBUH652pvxlY7CNLz0EVswlE1hIBD+Gn50nxVjSASDeIJPuOFsLd0rWQD'
    b'vwGZX5eIvM3txQAAAABJRU5ErkJggg==')

#----------------------------------------------------------------------
icons8_smartphone_ram_50 = PyEmbeddedImage(
    b'iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAA'
    b'5UlEQVRoge2YQQ7CIBBFX3tDvYj0jMZLVL1K6wIaF1ogJoUB/0smDWEW88N8SAeEECKwhrC6'
    b'D8CYSmiFboR0ywhMwIN3b1qLO+CAISZkMlBobriYkO0kTrGkypzxNc6xpCUkRY+tMgO+xiWW'
    b'lHVnG+Cjzpzr9wZcDa2/kiNkazcr6yy6bq0m+MUjpTnMI6WRR5pEHimIPNIk8khB5JEmkUcK'
    b'Io80if7ZK66z6MYj26b1AR0khDzD1+rIdMCPTMGPd3dx1B9O58YlpdjhB8S1C92LOYiw3P7H'
    b'krrJau8Df/ayCyGEHV4Hpj6QuXY7DQAAAABJRU5ErkJggg==')
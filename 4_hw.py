class Priyamougilnik:
    width = 0
    height = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def P(self):
        return (self.width + self.height) * 2

    def S(self):
        return self.width * self.height

odin = Priyamougilnik(5, 8)
print(odin.P(), odin.S())

dva = Priyamougilnik(7, 1)
print(dva.P(), dva.S())

tri = Priyamougilnik(8, 2)
print(tri.P(), tri.S())


class Math:
    a = 0
    b = 0

    def __init__(self, pervoe, vtoroe):
        self.a = pervoe
        self.b = vtoroe

    def addition(self):
        return self.a + self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        if(self.b == 0):
            assert 0, "Can`t divide by 0"
        return self.a / self.b

    def subtraction(self):
        return self.a - self.b

obect = Math(1, 2)
print(obect.addition(), obect.multiplication(), obect.division(), obect.subtraction())


class Button:
    buttonText = ""
    buttonType = "button"
    buttonLocator = ""

    def __init__(self, text):
        self.buttonText = text

    def press(self):
        return "klick po knopke" + self.buttonText

TextBox = Button("Text Box")
print(TextBox.buttonText)
TextBox.press()

CheckBox = Button("Check Box")
print(CheckBox.buttonText)
CheckBox.press()

RadioButton = Button("Radio Button")
print(RadioButton.buttonText)
RadioButton.press()

WebTables = Button("Web Tables")
print(WebTables.buttonText)
WebTables.press()

Buttons = Button("Buttons")
print(Buttons.buttonText)
Buttons.press()

Links = Button("Links")
print(Links.buttonText)
Links.press()

BrokenLinks = Button("Broken Links - Images")
print(BrokenLinks.buttonText)
BrokenLinks.press()

UploadandDownload = Button("Upload and Download")
print(UploadandDownload.buttonText)
UploadandDownload.press()

DynamicProperties = Button("Dynamic Properties")
print(DynamicProperties.buttonText)
DynamicProperties.press()
# Device Situation Choices in Model Files
DEVICE_STATUS = (
    ('at Technical Service', 'at Technical Service'),
    ('Ready to Delivery', 'Ready to Delivery'),
    ('Delivered', 'Delivered'),
)

# Device Brand Choices
# Admin can leave the field blank if device is laptop, oem or other type device
DEVICE_BRANDS = (
    ('LAPTOP', (
        ('Acer', 'Acer'),
        ('Asus', 'Asus'),
        ('Casper', 'Casper'),
        ('Dell', 'Dell'),
        ('Exper', 'Exper'),
        ('Fujitsu', 'Fujitsu'),
        ('Gigabyte', 'Gigabyte'),
        ('Hashtab', 'Hashtab'),
        ('Hp', 'Hp'),
        ('Lenovo', 'Lenovo'),
        ('Monster', 'Monster'),
        ('MSI', 'MSI'),
        ('Packard Bell', 'Packard Bell'),
        ('Samsung', 'Samsung'),
        ('Sony', 'Sony'),
        ('Toshiba', 'Toshiba'),
        ('Trust', 'Trust'),
        ('Other', 'Other'),
        )
    ),

    ('MAC', (
        ('Apple', 'Apple'),
        )
    ),

    ('IPHONE', (
        ('Apple', 'Apple'),
        )
    ),

    ('ANDROID PHONE', (
        ('Alcatel', 'Alcatel'),
        ('Asus', 'Asus'),
        ('Avea', 'Avea'),
        ('Casper', 'Casper'),
        ('Dark', 'Dark'),
        ('Euo', 'Euo'),
        ('Fly', 'Fly'),
        ('General Mobile', 'General Mobile'),
        ('Gigabyte GSmart', 'Gigabyte GSmart'),
        ('Google', 'Google'),
        ('HTC', 'HTC'),
        ('Huwaei', 'Huwaei'),
        ('LG', 'LG'),
        ('Motorola', 'Motorola'),
        ('Philips', 'Philips'),
        ('Piranha', 'Piranha'),
        ('Prestigio', 'Prestigio'),
        ('Samsung', 'Samsung'),
        ('Sony', 'Sony'),
        ('Turkcell', 'Turkcell'),
        ('Utoo', 'Utoo'),
        ('Vodafone', 'Vodafone'),
        ('ZTE', 'ZTE'),
        ('Other', 'Other'),
        )
    ),

    ('WINDOWSPHONE',(
        ('Alcatel', 'Alcatel'),
        ('Asus', 'Asus'),
        ('Avea', 'Avea'),
        ('Casper', 'Casper'),
        ('Dark', 'Dark'),
        ('Euo', 'Euo'),
        ('Fly', 'Fly'),
        ('General Mobile', 'General Mobile'),
        ('Gigabyte GSmart', 'Gigabyte GSmart'),
        ('Google', 'Google'),
        ('HTC', 'HTC'),
        ('Huwaei', 'Huwaei'),
        ('LG', 'LG'),
        ('Motorola', 'Motorola'),
        ('Nokia', 'Nokia'),
        ('Philips', 'Philips'),
        ('Piranha', 'Piranha'),
        ('Prestigio', 'Prestigio'),
        ('Samsung', 'Samsung'),
        ('Sony', 'Sony'),
        ('Turkcell', 'Turkcell'),
        ('Utoo', 'Utoo'),
        ('Vodafone', 'Vodafone'),
        ('ZTE', 'ZTE'),
        ('Other', 'Other'),
        )
    ),

    ('BLACKBERRY', (
        ('Blackberry', 'Blackberry'),
        )
    ),

    ('IPAD', (
        ('Apple', 'Apple'),
        )
    ),

    ('ANDROID TABLET', (
        ('Acer', 'Acer'),
        ('Artes', 'Artes'),
        ('Asus', 'Asus'),
        ('Casper', 'Casper'),
        ('Codegen', 'Codegen'),
        ('Dark', 'Dark'),
        ('Dell', 'Dell'),
        ('Escort', 'Escort'),
        ('Everest', 'Everest'),
        ('Everpad', 'Everpad'),
        ('Exper', 'Exper'),
        ('Ezcool', 'Ezcool'),
        ('Firebrand', 'Firebrand'),
        ('Fujitsu', 'Fujitsu'),
        ('General Mobile', 'General Mobile'),
        ('GoSmart', 'GoSmart'),
        ('Hi-Level', 'Hi-Level'),
        ('HomeTech', 'HomeTech'),
        ('Hp', 'Hp'),
        ('Inca', 'Inca'),
        ('Jatter', 'Jatter'),
        ('Lenovo', 'Lenovo'),
        ('LG', 'LG'),
        ('Me', 'Me'),
        ('Mobee', 'Mobee'),
        ('Navitech', 'Navitech'),
        ('Next', 'Next'),
        ('Oblio', 'Oblio'),
        ('Onyo', 'Onyo'),
        ('Piranha', 'Piranha'),
        ('PolyPad', 'PolyPad'),
        ('Prestigio', 'Prestigio'),
        ('Pro2000', 'Pro2000'),
        ('Probook', 'Probook'),
        ('Qpad', 'Qpad'),
        ('Quadro', 'Quadro'),
        ('Reedpad', 'Reedpad'),
        ('Samsung', 'Samsung'),
        ('Sony', 'Sony'),
        ('Toshiba', 'Toshiba'),
        ('Unitab', 'Unitab'),
        ('Vippad', 'Vippad'),
        ('Other', 'Other'),
        )
    ),

    ('WINDOWS TABLET', (
        ('Acer', 'Acer'),
        ('Artes', 'Artes'),
        ('Asus', 'Asus'),
        ('Casper', 'Casper'),
        ('Codegen', 'Codegen'),
        ('Dark', 'Dark'),
        ('Dell', 'Dell'),
        ('Escort', 'Escort'),
        ('Everest', 'Everest'),
        ('Everpad', 'Everpad'),
        ('Exper', 'Exper'),
        ('Ezcool', 'Ezcool'),
        ('Firebrand', 'Firebrand'),
        ('Fujitsu', 'Fujitsu'),
        ('General Mobile', 'General Mobile'),
        ('GoSmart', 'GoSmart'),
        ('Hi-Level', 'Hi-Level'),
        ('HomeTech', 'HomeTech'),
        ('Hp', 'Hp'),
        ('Inca', 'Inca'),
        ('Jatter', 'Jatter'),
        ('Lenovo', 'Lenovo'),
        ('LG', 'LG'),
        ('Me', 'Me'),
        ('Mobee', 'Mobee'),
        ('Navitech', 'Navitech'),
        ('Next', 'Next'),
        ('Oblio', 'Oblio'),
        ('Onyo', 'Onyo'),
        ('Piranha', 'Piranha'),
        ('PolyPad', 'PolyPad'),
        ('Prestigio', 'Prestigio'),
        ('Pro2000', 'Pro2000'),
        ('Probook', 'Probook'),
        ('Qpad', 'Qpad'),
        ('Quadro', 'Quadro'),
        ('Reedpad', 'Reedpad'),
        ('Samsung', 'Samsung'),
        ('Sony', 'Sony'),
        ('Toshiba', 'Toshiba'),
        ('Unitab', 'Unitab'),
        ('Vippad', 'Vippad'),
        ('Other', 'Other'),
        )
    ),
    ('Unknown', 'Unknown')
)

# Device Type Choices
DEVICE_TYPES = (
    ('DESKTOP', (
        ('Desktop', 'Desktop'),
        )
    ),

    ('LAPTOP', (
        ('Laptop', 'Laptop'),
        ('Ultrabook', 'Ultrabook'),
        ('Netbook', 'Netbook'),
        ('Gamebook', 'Gamebook'), 
        )
    ),

    ('MAC', (
        ('MacBook Air', 'MacBook Air'),
        ('MacBook Pro', 'MacBook Pro'),
        ('Mac mini', 'Mac mini'),
        ('iMac', 'iMac'),
        ('Mac Pro', 'Mac Pro'),
        ('OS X Mavericks', 'OS X Mavericks'),
        )
    ),

    ('MOBILE DEVICE', (
        ('iPhone', 'iPhone'),
        ('Android Phone', 'Android Phone'),
        ('WindowsPhone', 'WindowsPhone'),
        ('Blackberry', 'Blackberry'),
        ('iPad', 'iPad'),
        ('Android Tablet', 'Android Tablet'),
        ('Windows Tablet', 'Windows Tablet'),
        ('Other', 'Other'),
        )
    ),

    ('OEM', (
        ('Oem Device', 'Oem Device'),
        )
    ),

    ('OTHER', (
        ('Other', 'Other'),
        )
    ),

    ('Unknown', 'Unknown')
)

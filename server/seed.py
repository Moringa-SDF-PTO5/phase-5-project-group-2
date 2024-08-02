from app import app, db
from models import User, Staff, Category, Product, Order, OrderItem, Address, Payment

def seed_database():
    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()

        # Create sample users
        users = [
            User(username='admin', password='adminpassword', email='admin@example.com', role='admin'),
            User(username='customer1', password='customerpassword', email='customer1@example.com', role='customer'),
            User(username='customer2', password='customerpassword', email='customer2@example.com', role='customer')
        ]
        db.session.bulk_save_objects(users)
        db.session.commit()
        
        # Create sample staff
        staffs= [
            {'first_name': 'John', 'last_name': 'Doe', 'email': 'john.doe@example.com', 'role': 'Manager'},
            {'first_name': 'Jane', 'last_name': 'Smith', 'email': 'jane.smith@example.com', 'role': 'Developer'},
            {'first_name': 'Alice', 'last_name': 'Johnson', 'email': 'alice.johnson@example.com', 'role': 'Analyst'},
        ]
        for staff_data in staffs:
            staff = Staff(**staff_data)
            db.session.add(staff)
        db.session.commit()

        # Create sample categories
        categories = [
            Category(category_name='Tablets', description='Versatile tablets for work and play.'),
            Category(category_name='Headphones', description='Top quality headphones for the best sound experience.'),
            Category(category_name='Cameras', description='High-resolution cameras for photography enthusiasts.'),
            Category(category_name='Laptops', description='High-performance laptops for all needs.'),
            Category(category_name='Smartphones', description='Latest smartphones with cutting-edge technology.'),
            Category(category_name='Home Appliances', description='Various home appliances for everyday use.')
        ]
        db.session.bulk_save_objects(categories)
        db.session.commit()

        # Create sample products
        products = [
            Product(name='Tablet Z3', image='https://m.media-amazon.com/images/I/51gj5oQXbnL._AC_UY327_FMwebp_QL65_.jpg', description='A versatile tablet for productivity and entertainment.', price=49009.99, category_id=1,  stock_quantity=75),
            Product(name='Amazon Fire HD 10', image='https://m.media-amazon.com/images/I/51-6uBmjPqL._AC_UY327_FMwebp_QL65_.jpg', description='built for relaxation, 10.1" vibrant Full HD screen, octa-core processor, 3 GB RAM, latest model (2023 release), 32 GB, Ocean', price=12000.00, category_id=1,  stock_quantity=15),
            Product(name='Amazon Fire HD 8 Kids tablet', image='https://m.media-amazon.com/images/I/51OjR-ZoH9L._AC_UY327_FMwebp_QL65_.jpg', description='ages 3-7. Top-selling 8" kids tablet on Amazon - 2022 | ad-free content with parental controls included, 13-hr battery, 32 GB, Blue', price=10000.00, category_id=1,  stock_quantity=22),
            Product(name='SAMSUNG Galaxy Tab A9+ Plus 11', image='https://m.media-amazon.com/images/I/61h+qeD-qfL._AC_UY327_FMwebp_QL65_.jpg', description='64GB Android Tablet, Big Screen, Quad Speakers, Upgraded Chipset, Multi Window Display, Slim, Light, Durable, Kids Friendly Design, US Version, 2024, Silver', price=13000.00, category_id=1,  stock_quantity=19),
            Product(name='SAMSUNG Galaxy Tab S6 Lite (2024)', image='https://m.media-amazon.com/images/I/71-hJGtkLWL._AC_SY450_.jpg', description='.4" 64GB WiFi Android Tablet, S Pen Included, Gaming Ready, Long Battery Life, Slim Metal Design, Expandable Storage, US Version, Oxford Gray', price=9000.00, category_id=1, stock_quantity=42),
            Product(name='Xgody 10.1 Inch Tablet', image='https://m.media-amazon.com/images/I/71s1jKqZGVL.__AC_SX300_SY300_QL70_FMwebp_.jpg', description='Android 13,12GB RAM+128GB ROM(TF 1TB), Quad-Core 2.0 GHz,WiFi 5G/2.4G,GMS, Battery 7000mAh,Dual Camera 13MP+5MP,Tablet with Case,Keyboard,Pen - Grey', price=12000.00, category_id=1,  stock_quantity=45),
            Product(name='UMIDIGI G1 Tab Android 13 Tablet 2024', image='https://m.media-amazon.com/images/I/71VZUjB-bzL._AC_SY450_.jpg', description='8(4+4) GB+64GB 1TB Expand, 5G/2.4G WiFi, 10.1 inch HD Tablet with Quad-Core Processor up to 2.0 GHz, 6000mAh, Dual Camera, BT, 1280 * 800 Touch Screen', price=15000.00, category_id=1,  stock_quantity=34),
            Product(name='Amazon Fire HD 8 tablet', image='https://m.media-amazon.com/images/I/61fgc1OW1ZL._AC_UY327_FMwebp_QL65_.jpg', description='” HD Display, 64 GB, 30% faster processor, designed for portable entertainment, (2022 release), Black', price=14000.00, category_id=1,  stock_quantity=30),
            Product(name='Amazon Fire HD 10 tablet', image='https://m.media-amazon.com/images/I/51-6uBmjPqL._AC_UY327_FMwebp_QL65_.jpg', description='built for relaxation, 10.1" vibrant Full HD screen, octa-core processor, 3 GB RAM, latest model (2023 release), 32 GB, Ocean', price=12000.00, category_id=1,  stock_quantity=23),
            Product(name='Lenovo Tab M8 (4th Gen)', image='https://m.media-amazon.com/images/I/61e2XEOJLGL._AC_UY327_FMwebp_QL65_.jpg', description='2023 - Tablet - Long Battery Life - 8" HD - Front 2MP & Rear 5MP Camera - 2GB Memory - 32GB Storage - Android 12 (Go Edition) or Later,Gray', price=23000.00, category_id=1,  stock_quantity=25),
            Product(name='Samsung Galaxy Tab A9 (SM-X110)', image='https://m.media-amazon.com/images/I/51HL5sz4keL._AC_UY327_FMwebp_QL65_.jpg', description='64GB 4GB RAM, WiFi Only, Factory Unlocked GSM, International Version (15W Wall Charger Bundle) (Gray)', price=16000.00, category_id=1,  stock_quantity=20),
            Product(name='Headphones A4', image='https://m.media-amazon.com/images/I/61O7S27O+jL._AC_UY327_FMwebp_QL65_.jpg', description='Noise-cancelling headphones for a superior listening experience.', price=19900.99, category_id=2, stock_quantity=150),
            Product(name='Camera B5', image='https://m.media-amazon.com/images/I/713rZRWpnPL._AC_UY327_FMwebp_QL65_.jpg', description='A high-resolution camera for capturing stunning photos.', price=119009.99, category_id=3, stock_quantity=30),
            Product(name='HP Laptop', image='https://m.media-amazon.com/images/I/71CDSpds6jL._AC_UY327_FMwebp_QL65_.jpg', description='A powerful laptop with high-speed performance.', price=99009.99, category_id=4,  stock_quantity=50),
            Product(name='Moto G Smartphone', image='https://m.media-amazon.com/images/I/61K1Fz5LxvL._AC_UY327_FMwebp_QL65_.jpg', description='A sleek smartphone with the latest features.', price=79900.99, category_id=5, stock_quantity=100),
            Product(name='Amazon Fire TV', image='https://m.media-amazon.com/images/I/71Nma1KADeL._AC_UY327_FMwebp_QL65_.jpg', description='High-resolution smart TV.', price=50009.99, category_id=6, stock_quantity=50),
            Product(name='Google Pixel 7a', image='https://m.media-amazon.com/images/I/61r7cCpQPlL._AC_UY327_FMwebp_QL65_.jpg', description='Smartphone with Wide Angle Lens and 24-Hour Battery - 128 GB – Charcoal', price=40000.00, category_id=5,  stock_quantity=15),
            Product(name='SAMSUNG Galaxy A15', image='https://m.media-amazon.com/images/I/61s0ZzwzSCL._AC_UY327_FMwebp_QL65_.jpg', description='5G A Series Cell Phone, 128GB Unlocked Android Smartphone, AMOLED Display, Expandable Storage, Knox Security, Super Fast Charging, Hi-Res Camera, US Version, 2024, Blue Black', price=34000.00, category_id=5,  stock_quantity=22),
            Product(name='SAMSUNG Galaxy S24', image='https://m.media-amazon.com/images/I/71WcjsOVOmL._AC_UY327_FMwebp_QL65_.jpg', description='Ultra Cell Phone, 512GB AI Smartphone, Unlocked Android, 200MP, 100x Zoom Cameras, Long Battery Life, S Pen, US Version, 2024, Titanium Black', price=103000.00, category_id=5,  stock_quantity=19),
            Product(name='Motorola Edge | 2023', image='https://m.media-amazon.com/images/I/61w-1c1nOzL._AC_UY327_FMwebp_QL65_.jpg', description=' Unlocked | Made for US 8/256GB | 50MP Camera | Eclipse Black', price=39000.00, category_id=5,  stock_quantity=42),
            Product(name='SAMSUNG Galaxy A35', image='https://m.media-amazon.com/images/I/71lw4ZWUfYL._AC_UY327_FMwebp_QL65_.jpg', description='5G A Series Cell Phone, 128GB Unlocked Android Smartphone, AMOLED Display, Advanced Triple Camera System, Expandable Storage, Rugged Design, US Version, 2024, Awesome Lilac', price=27000.00, category_id=5,  stock_quantity=45),
            Product(name='Xiaomi Redmi Note 13 PRO', image='https://m.media-amazon.com/images/I/61vFWIksgcL._AC_UY327_FMwebp_QL65_.jpg', description='5G + 4G LTE (256GB + 8GB) 6.67" 200MP Triple (Tmobile Mint Tello & Global) GLOBAL Bands Unlocked + (Fast Car Dual Charger Bundle) (Aurora Purple (Global ROM))', price=45000.00, category_id=5,  stock_quantity=34),
            Product(name='Motorola Moto G 5G', image='https://m.media-amazon.com/images/I/61vgbLrWDyL._AC_UY327_FMwebp_QL65_.jpg', description='Made for US 4/128GB | 48 MPCamera | Ink Blue, 163.94x74.98x8.39', price=33000.00, category_id=5,  stock_quantity=30),
            Product(name='Google Pixel 8', image='https://m.media-amazon.com/images/I/81Mya-dPIOL._AC_UY327_FMwebp_QL65_.jpg', description='Unlocked Android Smartphone with Advanced Pixel Camera, 24-Hour Battery, and Powerful Security - Obsidian - 128 GB', price=32000.00, category_id=5,  stock_quantity=23),
            Product(name='OnePlus 12', image='https://m.media-amazon.com/images/I/711F6T6aySL._AC_UY327_FMwebp_QL65_.jpg', description='16GB RAM+512GB,Dual-SIM,Unlocked Android Smartphone,Supports 50W Wireless Charging,Latest Mobile Processor,Advanced Hasselblad Camera,5400 mAh Battery,2024,Flowy Emerald', price=43000.00, category_id=5,  stock_quantity=25),
            Product(name='SAMSUNG Galaxy Z', image='https://m.media-amazon.com/images/I/61896OtgvGL._AC_UY327_FMwebp_QL65_.jpg', description='Fold 6 AI Cell Phone, 512GB Unlocked Android Smartphone, Circle to Search, Handsfree Live Interpreter, AI Photo Edits, Large Screen, 2024,US 1 Yr Manufacturer Warranty, Navy', price=280000.00, category_id=5,  stock_quantity=20),
            Product(name='Soundcore Anker Life Q20', image='https://m.media-amazon.com/images/I/61O7S27O+jL._AC_SX466_.jpg', description='Hybrid Active Noise Cancelling Headphones, Wireless Over Ear Bluetooth Headphones, 60H Playtime, Hi-Res Audio, Deep Bass, Memory Foam Ear Cups, for Travel, Home Office', price=7000.00, category_id=2,  stock_quantity=15),
            Product(name='Bose QuietComfort', image='https://m.media-amazon.com/images/I/51QeS0jkx-L._AC_SY450_.jpg', description='Wireless Noise Cancelling Headphones, Bluetooth Over Ear Headphones with Up To 24 Hours of Battery Life, Black', price=40000.00, category_id=2,  stock_quantity=22),
            Product(name='Beats Studio Pro', image='https://m.media-amazon.com/images/I/61SNDXZcmTL._AC_UY327_FMwebp_QL65_.jpg', description='Wireless Bluetooth Noise Cancelling Headphones - Personalized Spatial Audio, USB-C Lossless Audio, Apple & Android Compatibility, Up to 40 Hours Battery Life - Deep Brown', price=19000.00, category_id=2,  stock_quantity=19),
            Product(name='Sony WH-CH720N', image='https://m.media-amazon.com/images/I/51rpbVmi9XL._AC_SY450_.jpg', description='Noise Canceling Wireless Headphones Bluetooth Over The Ear Headset with Microphone and Alexa Built-in, Black New', price=39000.00, category_id=2, stock_quantity=42),
            Product(name='Apple AirPods Max Wireless Over-Ear Headphones', image='https://m.media-amazon.com/images/I/81thV7SoLZL._AC_SX466_.jpg', description='ctive Noise Cancelling, Transparency Mode, Personalized Spatial Audio, Dolby Atmos, Bluetooth Headphones for iPhone – Silver', price=49000.00, category_id=2,  stock_quantity=45),
            Product(name='JBL TUNE 720BT', image='https://m.media-amazon.com/images/I/61EL2AKKcBL._AC_SY450_.jpg', description='Wireless over-ear headphones Pure Bass sound, Bluetooth 5.3, Up to 76H battery life and speed charge, Lightweight, comfortable and foldable design (Black)', price=9000.00, category_id=2,  stock_quantity=34),
            Product(name='Soundcore by Anker Q20i', image='https://m.media-amazon.com/images/I/51FfiLFD2oL._AC_UY327_FMwebp_QL65_.jpg', description='Hybrid Active Noise Cancelling Headphones, Wireless Over-Ear Bluetooth, 40H Long ANC Playtime, Hi-Res Audio, Big Bass, Customize via an App, Transparency Mode (WHITE)', price=8000.00, category_id=2,  stock_quantity=30),
            Product(name='Sony WH-1000XM4 ', image='https://m.media-amazon.com/images/I/51DkbWZIg+L._AC_SX450_.jpg', description='Wireless Premium Noise Canceling Overhead Headphones with Mic for Phone-Call and Alexa Voice Control, Black WH1000XM4', price=39000.00, category_id=2,  stock_quantity=23),
            Product(name='AILIHEN C8 Headphones ', image='https://m.media-amazon.com/images/I/71yzAE39cxL._AC_UY327_FMwebp_QL65_.jpg', description='Wired, On-Ear Headphones with Microphone and Volume Control Foldable Corded Stereo 3.5mm Headset for Smartphones Chromebook Laptop Computer PC Tablets Travel(Black/Blue)', price=2200.00, category_id=2,  stock_quantity=25),
            Product(name='Picun B8 Bluetooth Headphones', image='https://m.media-amazon.com/images/I/714leNyXHIL._AC_UY327_FMwebp_QL65_.jpg', description='120 Hours Headphones Wireless Bluetooth, Hands-Free Calls, 3EQ & Game Mode, Foldable Headphones Over Ear for Travel Home Office Cellphone PC', price=2700.00, category_id=2,  stock_quantity=20),
            Product(name='Video Camera Camcorder', image='https://m.media-amazon.com/images/I/71C6TFutbeL._AC_SY450_.jpg', description='Digital Camera Recorder Full HD 1080P 15FPS 24MP 3.0 Inch 270 Degree Rotation LCD 16X Digital Zoom Camcorder Camera with 2 Batteries(Black)', price=9050.00, category_id=3, stock_quantity=30),
            Product(name='ZEEPORTE Security Camera', image='https://m.media-amazon.com/images/I/61+FM2XQUyL._AC_SY450_.jpg', description='Security Cameras Wireless Outdoor, 2K Battery Powered WiFi Cameras for Home Security with AI Motion Detection, Color Night Vision, Spotlight, Siren, Waterproof, SD/Cloud Storage', price=6000.00, category_id=3,  stock_quantity=15),
            Product(name='Canon EOS R100 Mirrorless Camera', image='https://m.media-amazon.com/images/I/71edZl9AfcL._AC_UY327_FMwebp_QL65_.jpg', description='RF-S18-45mm F4.5-6.3 IS STM Lens Kit, 24.1 Megapixel CMOS (APS-C) sensor, 4K Video, RF Mount, Black', price=45000.00, category_id=3,  stock_quantity=22),
            Product(name='Saneen Digital Camera', image='https://m.media-amazon.com/images/I/71NXowebfKL._AC_UY327_FMwebp_QL65_.jpg', description='4k Cameras for Photography & Video, 64MP WiFi Touch Screen Vlogging Camera for YouTube with Flash, 32GB SD Card, Lens Hood, 3000mAH Battery, Front and Rear Cameras - Black', price=19000.00, category_id=3,  stock_quantity=19),
            Product(name='YI Pro 2K 4PC Home Security Camera', image='https://m.media-amazon.com/images/I/61iKXBiFBXL._AC_SY450_PIbundle-4,TopRight,0,0_SH20_.jpg', description='2.4Ghz Indoor IP Camera with Person, Vehicle, Animal Detection, Phone App for Baby, Pet, Dog Monitoring, Works with Alexa and Google Assistant', price=6000.00, category_id=3, stock_quantity=42),
            Product(name='VETEK Digital Cameras', image='https://m.media-amazon.com/images/I/71JfxR92onL._AC_SY450_.jpg', description='Cameras for Photography, 4K 48MP Vlogging Camera 16X Digital Zoom Manual Focus Students Compact Camera with 52mm Wide-Angle Lens & Macro Lens, 32G Micro Card and 2 Batteries (Pink)', price=13000.00, category_id=3,  stock_quantity=45),
            Product(name='Video Camera Camcorder', image='https://m.media-amazon.com/images/I/71C6TFutbeL._AC_UY327_FMwebp_QL65_.jpg', description='Digital Camera Recorder Full HD 1080P 15FPS 24MP 3.0 Inch 270 Degree Rotation LCD 16X Digital Zoom Camcorder Camera with 2 Batteries(Black)', price=7000.00, category_id=3,  stock_quantity=34),
            Product(name='KODAK PIXPRO AZ405-BK', image='https://m.media-amazon.com/images/I/71suGwfhN1L._AC_SY450_.jpg', description='20MP Digital Camera 40X Optical Zoom 24mm Wide Angle Lens Optical Image Stabilization 1080P Full HD Video 3" LCD Vlogging Camera (Black)', price=25000.00, category_id=3,  stock_quantity=30),
            Product(name='Canon EOS REBEL T7 DSLR Camera', image='https://m.media-amazon.com/images/I/71ZYxtmYkPL._AC_UY327_FMwebp_QL65_.jpg', description='2 Lens Kit with EF18-55mm + EF 75-300mm Lens, Black', price=68000.00, category_id=3,  stock_quantity=23),
            Product(name='KODAK PIXPRO WPZ2', image='https://m.media-amazon.com/images/I/61hVj7O9WrL._AC_UY327_FMwebp_QL65_.jpg', description='Rugged Waterproof Shockproof Dustproof WiFi Digital Camera 16MP 4X Optical Zoom 1080P Full HD Video Vlogging Camera 2.7" LCD (Yellow)', price=21000.00, category_id=3,  stock_quantity=25),
            Product(name='Kodak AZ401RD', image='https://m.media-amazon.com/images/I/71mcXgTbfjL._AC_UY327_FMwebp_QL65_.jpg', description='Point & Shoot Digital Camera with 3" LCD, Red', price=18000.00, category_id=3,  stock_quantity=20),
            Product(name='Lenovo Newest 15.6" Laptop', image='https://m.media-amazon.com/images/I/71sPoxApv4L._AC_UY327_FMwebp_QL65_.jpg', description='Intel Dual-core Processor, 16GB Memory, 1TB PCIe SSD, 15.6" FHD (1920 x 1080) Anti-Glare Display, HDMI, Ethernet Port, USB-C, Webcam, WiFi & Bluetooth, Windows 11 Pro', price=59009.99, category_id=4,  stock_quantity=50),
            Product(name='Lenovo IdeaPad 1 Laptop', image='https://m.media-amazon.com/images/I/51h3oOo7XnL._AC_UY327_FMwebp_QL65_.jpg', description='FHD Display, AMD Ryzen 5 5500U, 8GB RAM, 512GB SSD, Windows 11 Home, 720p Camera w/Privacy Shutter, Smart Noise Cancelling, Cloud Grey', price=40000.00, category_id=4,  stock_quantity=15),
            Product(name='ASUS 15.6” Vivobook Go Laptop', image='https://m.media-amazon.com/images/I/61KZBt8QeGL._AC_UY327_FMwebp_QL65_.jpg', description='Intel Celeron N4500, 4GB RAM, 128GB SSD, Windows 11 in S Mode, Star Black, L510KA-ES04', price=23000.00, category_id=4,  stock_quantity=22),
            Product(name='Acer Aspire 3 A315-24P-R7VH Slim Laptop', image='https://m.media-amazon.com/images/I/61gKkYQn6lL._AC_UY327_FMwebp_QL65_.jpg', description='15.6" Full HD IPS Display | AMD Ryzen 3 7320U Quad-Core Processor | AMD Radeon Graphics | 8GB LPDDR5 | 128GB NVMe SSD | Wi-Fi 6 | Windows 11 Home in S Model', price=34000.00, category_id=4,  stock_quantity=19),
            Product(name='HP Newest 14" Ultral Light', image='https://m.media-amazon.com/images/I/71GpA7p2KDL._AC_UY327_FMwebp_QL65_.jpg', description='Laptop for Students and Business, Intel Quad-Core N4120, 16GB RAM, 128GB Storage(64GB eMMC+64GB Ghost Manta SD), 1 Year Office 365, Webcam, HDMI, WiFi, USB-A&C, Win 11 S', price=39000.00, category_id=4, stock_quantity=42),
            Product(name='HP Portable Laptop', image='https://m.media-amazon.com/images/I/61IpRGnny7L._AC_SY450_.jpg', description='Suitable for Student and Business, 14" HD Display, Intel Quad-Core N4120, 8GB DDR4 RAM, 64GB eMMC, 1 Year Office 365, Webcam, RJ-45, HDMI, Wi-Fi, Windows 11 Home, Silver', price=25000.00, category_id=4,  stock_quantity=45),
            Product(name='Acer Aspire Go 15 Slim Laptop', image='https://m.media-amazon.com/images/I/71hFmMzygKL._AC_UY327_FMwebp_QL65_.jpg', description='15.6" Full HD IPS 1080P Display | Intel Core i3-N305| Intel UHD Graphics | 8GB LPDDR5 | 128GB HD | Wi-Fi 6 | AI PC | Windows 11 Home in S Mode | AG15-31P-3947', price=30000.00, category_id=4,  stock_quantity=34),
            Product(name='HP 17 Business Laptop', image='https://m.media-amazon.com/images/I/61TGRBGTNzL._AC_UY327_FMwebp_QL65_.jpg', description='17.3” HD+ Display, 11th Gen Intel Core i3-1125G4 Processor, 32GB RAM, 1TB SSD, Wi-Fi, HDMI, Webcam, Windows 11 Pro, Silver', price=54000.00, category_id=4,  stock_quantity=30),
            Product(name='HP Notebook Laptop', image='https://m.media-amazon.com/images/I/61oAh3XrX+L._AC_SY450_.jpg', description='15.6" HD Touchscreen, Intel Core i3-1115G4 Processor, 32GB RAM, 1TB PCIe SSD, Webcam, Type-C, HDMI, SD Card Reader, Wi-Fi, Windows 11 Home, Silver', price=49000.00, category_id=4,  stock_quantity=23),
            Product(name='HP 14 inch Laptop', image='https://m.media-amazon.com/images/I/81tnwNLrlDL._AC_UY327_FMwebp_QL65_.jpg', description='HD Display, 12th Generation Intel Core i3-1215U, 8 GB RAM, 256 GB SSD, Intel UHD Graphics, Windows 11 Home in S mode, 14-dq5009nr (2024)', price=40000.00, category_id=4,  stock_quantity=25),
            Product(name='ASUS ROG Strix G16 (2024) Gaming Laptop', image='https://m.media-amazon.com/images/I/81GrCeuCzxL._AC_UY327_FMwebp_QL65_.jpg', description='16” 16:10 FHD 165Hz Display, NVIDIA® GeForce RTX™ 4060, Intel Core i7-13650HX, 16GB DDR5, 1TB PCIe Gen4 SSD, Wi-Fi 6E, Windows 11, G614JV-AS74', price=130000.00, category_id=4,  stock_quantity=20),
            Product(name='Vacuum Sealer Machine', image='https://m.media-amazon.com/images/I/71HVxIsLG6L._AC_UL480_FMwebp_QL65_.jpg', description='90Kpa Food Vacuum Sealer Machine Preservation Dry/Moist/Liquid Modes, LED Indicator Light, Handle Locked Design, Built-in Cutter and Bag Storage, Removable Drip Tray', price=17000.00, category_id=6, stock_quantity=50),
            Product(name='Nuwave Infinity Commercial Blender', image='https://m.media-amazon.com/images/I/71FMtKL1X8L._AC_UL480_FMwebp_QL65_.jpg', description='Heavy-Duty Smoothie Blender w/ 2.5HP Copper Motor & Laser-Cut Blades, Last 100 Years, Quick Ice Crushing, 64oz Tritan Jar, NSF Certified, 10 Speeds, Self-Cleaning', price=28000.00, category_id=6,  stock_quantity=15),
            Product(name='Hamilton Beach Electric Indoor Searing Grill', image='https://m.media-amazon.com/images/I/81R5ZsXZoML._AC_UL480_FMwebp_QL65_.jpg', description='Grill with Adjustable Temperature Control to 450F, Removable Nonstick Grate, 118 sq. in. Surface Serves 6, Stainless Steel', price=9500.00, category_id=6,  stock_quantity=22),
            Product(name='Homvana Humidifiers for Bedroom Home', image='https://m.media-amazon.com/images/I/61k8GrdmN7L.__AC_SX300_SY300_QL70_FMwebp_.jpg', description='3.6L Cool Mist Top-Fill 34H Super Long Time, Quiet 23dB, Baby Humidifier, Oil Diffuser for Large Room, Plants, Nursery, Office BPA FREE, 7 Color Light Ultrasonic', price=5000.00, category_id=6,  stock_quantity=19),
            Product(name='Cuisinart Air Fryer Oven', image='https://m.media-amazon.com/images/I/71WOxmndFvL._AC_SX679_.jpg', description='6-Qt Basket Stainless Steel Air Fryer – Dishwasher-Safe Parts with 5 Presets – Roast, Bake, Broil, Air Fry and Keep Warm – Quick & Easy Meals – AIR-200', price=17000.00, category_id=6, stock_quantity=42),
            Product(name='Mueller Retro Toaster', image='https://m.media-amazon.com/images/I/819hb8UxwLL._AC_UL480_FMwebp_QL65_.jpg', description=' Slice with 7 Browning Levels and 3 Functions: Reheat, Defrost & Cancel, Stainless Steel Features, Removable Crumb Tray, Under Base Cord Storage, Black', price=3000.00, category_id=6,  stock_quantity=45),
            Product(name='Ninja CFP307 DualBrew Pro Specialty Coffee System', image='https://m.media-amazon.com/images/I/81-vMuZ92ZL._AC_UL480_FMwebp_QL65_.jpg', description='Single-Serve, Compatible with K-Cup Pods, and 12-Cup Drip Coffee Maker, with Permanent Filter', price=23000.00, category_id=6,  stock_quantity=34),
            Product(name='Air Purifiers for Bedroom Pets Smokers in Home', image='https://m.media-amazon.com/images/I/61PYRO1Do8L._AC_UL480_FMwebp_QL65_.jpg', description='H13 True HEPA Filter Air Cleaner with Fragrance Sponge, Night Light, Timer, Effectively Clean 99.97% Smoke, Dust, Pollen, Pet Dander, Odors, BS-01 Black', price=5000.00, category_id=6,  stock_quantity=30),
            Product(name='3.5 Cu. Ft. Capacity Double-door Compact Fridge', image='https://m.media-amazon.com/images/I/61x64u2sSiL._AC_SX679_.jpg', description='with Freezer and 7-Level Thermostat, Compact Convenience and Energy Savings, Ideal for Apartments, Dorms, Home Offices and Bars, Black Color', price=26000.00, category_id=6,  stock_quantity=23),
            Product(name='BLACK+DECKER 6-Cup Rice Cooker', image='https://m.media-amazon.com/images/I/61LP09dUn9L._AC_UY327_QL65_.jpg', description='RC506, 3-cup Uncooked Rice, Steaming Basket, Removable Non-Stick Bowl, One Touch', price=3000.00, category_id=6,  stock_quantity=25),
            Product(name='Portable Washing Machine', image='https://m.media-amazon.com/images/I/61CGq0CqDwL._AC_SX679_.jpg', description='13.3lbs Automatic Laundry Machine with 10 Programs, LED Display, High-efficiency Compact Washer for Apartment, Home, Dorms, Rv, Grey', price=70000.00, category_id=6,  stock_quantity=20)
            
        ]
        db.session.bulk_save_objects(products)
        db.session.commit()

        # Create sample orders
        orders = [
            Order(user_id=2, total_amount=1299.98, status='completed'),
            Order(user_id=3, total_amount=499.99, status='pending')
        ]
        db.session.bulk_save_objects(orders)
        db.session.commit()

        # Create sample order items
        order_items = [
            OrderItem(order_id=1, product_id=1, quantity=1, price=999.99),
            OrderItem(order_id=1, product_id=2, quantity=1, price=199.99),
            OrderItem(order_id=2, product_id=3, quantity=1, price=499.99)
        ]
        db.session.bulk_save_objects(order_items)
        db.session.commit()

        # Create sample addresses
        addresses = [
            Address(user_id=2, street='123 Main St', city='Anytown', state='CA', postal_code='12345', country='USA'),
            Address(user_id=3, street='456 Elm St', city='Othertown', state='TX', postal_code='67890', country='USA')
        ]
        db.session.bulk_save_objects(addresses)
        db.session.commit()

        # Create sample payments
        payments = [
            Payment(order_id=1, amount=1199.98, payment_method='Credit Card', transaction_id='tx1234567890'),
            Payment(order_id=2, amount=499.99, payment_method='PayPal', transaction_id='tx0987654321')
        ]
        db.session.bulk_save_objects(payments)
        db.session.commit()

        print("Database seeded with users, staff, categories, products, orders, order items, addresses, and payments.")

if __name__ == "__main__":
    seed_database()

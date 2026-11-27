# textkit

## วัตถุประสงค์

ชุดฟังก์ชันพื้นฐานสำหรับจัดการข้อความ พัฒนาโดยสมาชิกทีม 4 คน

## การใช้งาน

```bash
python3 main.py
```

## โมดูล

### counter.py (สมาชิก 1)

ฟังก์ชัน `count_words(text)` นับจำนวนคำที่คั่นด้วยช่องว่าง เช่น `count_words("hello first year")` ได้ `3` และ `count_words("")` ได้ `0`

### reverser.py (สมาชิก 2)

ฟังก์ชัน `reverse_words(text)` กลับลำดับคำและจัดช่องว่างระหว่างคำให้เหลือหนึ่งช่อง

- `reverse_words("hello first year")` ได้ `year first hello`
- `reverse_words("a  b")` ได้ `b a`

### cleaner.py (สมาชิก 3)

ฟังก์ชัน 'clean_text(text)' จัดระเบียบช่องว่างในข้อความให้เป็นมาตรฐานเดียวกัน เช่น clean_text("hello first   year") ได้ 'hello first year'

### caser.py (สมาชิก 4)

ฟังก์ชัน `capitalize_words(text)` ทำให้อักษรตัวแรกของแต่ละคำเป็นตัวพิมพ์ใหญ่ เช่น `capitalize_words("hello first year")` ได้ `"Hello First Year"`

## ผู้จัดทำ

### สมาชิก 1

69114540426 นายวีรพัฒน์ เหลื่อมล้ำ

### สมาชิก 2

69114540017 นายจารุเดช บุญตั้ง

### สมาชิก 3

69114540080 นางสาวณัฏฐภัทร บุญเหลือ

### สมาชิก 4

69114540118 นายถกลเกียรติ โสดา



data = "ini adalah string"
print(data)
print(type(data))


#1. cara membuat string
'''

1. dengan menggunakan single quote '...'
2. dengan menggunakan double qoute "..."
'''


data = 'menggunakan single qoute'
print(data)


data = 'Menggunakan single qoute'
print(data)
print("Halo, apa kabar?")
print("Halo, apa kabar?")
print("ini adalah hari Selasa")

#2. Menggunakan tanda \


#Membuat tanda 'menjadi string
print('mari shalat Jum\'at')
print('g\'day, isn\'t it?')


#backlash
print("C:\\user\\Iqbal")


#tab
print("Iqbal\t\tsigit, semakin jauhan")

#backspace
print("Iqbal\bNugroho, jadi deketan")

#newline
print("baris pertama.\nbaris kedua.") # LF-> line feed -> unix, macos, linux
print("baris pertama.\rbaris kedua.") #CR -> carriage return -> commodore, acorn, lisp
print("baris pertama.\r\nbaris kedua.") # CRLF -> line feed carriage return -> dipakai oleh windows


#3. String literal atau raw


#hati-hati
print('C:\new folder') #alan salah pathnya

#menggunakan raw string
print(r'C:\new folder')

#multiline literal string
print(""""
Nama : Iqbal
Kelas : 3 SMA
""")

#muiltiline literal sting dan RAW
print(r"""
Nama : Iqbal
Kelas : 3 SMA\new normal
Website : www.iqbal.com/newID
""")
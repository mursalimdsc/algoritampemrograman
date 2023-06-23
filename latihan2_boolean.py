#setting variabel identitas
nim     = input("Masukkan NIM           : ")
nama    = input("Masukkan Nama Lengkap  : ")
kelas   = input("Masukkan Kelas         : ")
prodi   = input("Masukkan Nama Prodi    : ")

#setting variabel nilai
bhs_ind = int(input("Nilai Bahasa Indonesia : "))
bhs_ing = int(input("Nilai Bahasa Inggris   : "))
pd      = int(input("Nilai Pemrograman Dasar: "))
mtk     = int(input("Nilai Matematika       : "))
kal1    = int(input("Nilai Kalkulus 1       : "))

#perhitungan
rata = (bhs_ind+bhs_ing+pd+mtk+kal1)/5

if(rata >0 and rata <=60):
    grade_rata = ("C")
elif(rata > 60 and rata <=75):
    grade_rata = ("B")
elif(rata >75 and rata <=85):
    grade_rata = ("AB")
elif(rata > 85 and rata <=100):
    grade_rata = ("A")
else:
    grade_rata =("Grade Anda Tidak ditemukan!")



#menampilkan
print("------------------------------------------")
print("               KARTU HASIL STUDI       ")
print("------------------------------------------")
print ("Nim             :",nim)
print ("Nama lengkap    :",nama)
print ("kelas           :",kelas)
print ("Program studi   :",prodi)
print ("------------------------------------------")
print ("No    Nama Makul        Nilai      Grade  ")
print ("------------------------------------------")
print ("1.  Bahasa Indonesia  ",bhs_ind)    
print ("2.  Bahasa Inggris    ",bhs_ing)
print ("3.  Pemrograman Dasar ",pd)
print ("4.  Matematika        ",mtk)
print ("5.  Kalkulus 1        ",kal1)
print ("------------------------------------------")
print ("Rata-Rata             ",rata," ",grade_rata)
print ("------------------------------------------")

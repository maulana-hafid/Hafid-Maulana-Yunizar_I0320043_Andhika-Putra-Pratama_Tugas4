#Soal 4
print('Masukkan umur anda ! ')
umur = (input('Berapa umurmu : '))
print('Apakah anda sudah lulus ujian ? (Y /T)')
Jawab = (input('Jawab :')).upper()

if umur >= '21' :
    if Jawab == 'Y' :
        print('Anda dapat mendaftar di kursus ini')
    else :
        print('Anda tidak dapat mendaftar dikursus ini')

else :
    print('Anda tidak dapat mendaftar dikursus ini')
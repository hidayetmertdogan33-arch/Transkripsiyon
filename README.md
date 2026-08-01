BİLGİLER:
Bu uygulama bilgisayarınızın mikrofonunu, bazı dosyalarını, kütüphanelerini kullanır. Bunu kabul etmiyorsanız lütfen bu
uygulamayı silin. Uygulamayı silmeyerek, kullanarak bunu kabul etmiş olursunuz. Bu uygulama bilgisayarınıza "output.wav"
adlı dosya yükler. Bu dosya kritik değildir ancak bu kodun ürettiği, üreteceği tüm verileri, kodun ticari amaçla kullanmak, 
yazılı izinsiz yayınlamak vb. yasaktır. Kullanma klavuzunda değiştirebilirsiniz diye belirtilmeyen bir yeri değiştirmek
bilgisayarınızda hasara, kodun düzgün çalışmamasına sebep olabilir ve yasaktır.





KULLANMA KLAVUZU:
Satır 11:   duraction 5        5 sayısı kaç saniye kaydedeciğini belirtir, değiştirebilirsiniz.

Satır 28: text = recognizer.recognize_google(audio, language="tr") tr kısmı giriş dilini belirtir TRANSLATE.md dosyasındaki dil kodlarına göre değiştirebilirsiniz.

Satır 37:                   translated = GoogleTranslator(source='tr', target='es').translate(text)
Burada belirttiğimiz yerler dil tablosuna göre değiştirilebilir    -            -
TR Türkçe'yi ifade eder. ES İspanyolca'yı ifade eder. TR metin dili ES ise çıkış dili ifade eder.

Başka bir yeri lütfen değiştirmeyin. Değiştirmek yasaktır.

Eğer değiştirmeye vaktiniz yok ise lütfen PRO sürümünü kullanın.

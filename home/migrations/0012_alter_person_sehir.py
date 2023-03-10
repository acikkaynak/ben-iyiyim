# Generated by Django 4.1.6 on 2023-02-12 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_alter_person_notlar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='sehir',
            field=models.CharField(choices=[('Adana', 'Adana'), ('Adıyaman', 'Adıyaman'), ('Afyonkarahisar', 'Afyonkarahisar'), ('Ağrı', 'Ağrı'), ('Aksaray', 'Aksaray'), ('Amasya', 'Amasya'), ('Ankara', 'Ankara'), ('Antalya', 'Antalya'), ('Ardahan', 'Ardahan'), ('Artvin', 'Artvin'), ('Aydın', 'Aydın'), ('Balıkesir', 'Balıkesir'), ('Bartın', 'Bartın'), ('Batman', 'Batman'), ('Bayburt', 'Bayburt'), ('Bilecik', 'Bilecik'), ('Bingöl', 'Bingöl'), ('Bitlis', 'Bitlis'), ('Bolu', 'Bolu'), ('Burdur', 'Burdur'), ('Bursa', 'Bursa'), ('Çanakkale', 'Çanakkale'), ('Çankırı', 'Çankırı'), ('Çorum', 'Çorum'), ('Denizli', 'Denizli'), ('Diyarbakır', 'Diyarbakır'), ('Düzce', 'Düzce'), ('Edirne', 'Edirne'), ('Elazığ', 'Elazığ'), ('Erzincan', 'Erzincan'), ('Erzurum', 'Erzurum'), ('Eskişehir', 'Eskişehir'), ('Gaziantep', 'Gaziantep'), ('Giresun', 'Giresun'), ('Gümüşhane', 'Gümüşhane'), ('Hakkari', 'Hakkari'), ('Hatay', 'Hatay'), ('Iğdır', 'Iğdır'), ('Isparta', 'Isparta'), ('İstanbul', 'İstanbul'), ('İzmir', 'İzmir'), ('Kahramanmaraş', 'Kahramanmaraş'), ('Karabük', 'Karabük'), ('Karaman', 'Karaman'), ('Kars', 'Kars'), ('Kastamonu', 'Kastamonu'), ('Kayseri', 'Kayseri'), ('Kırıkkale', 'Kırıkkale'), ('Kırklareli', 'Kırklareli'), ('Kırşehir', 'Kırşehir'), ('Kilis', 'Kilis'), ('Kocaeli', 'Kocaeli'), ('Konya', 'Konya'), ('Kütahya', 'Kütahya'), ('Malatya', 'Malatya'), ('Manisa', 'Manisa'), ('Mardin', 'Mardin'), ('Mersin', 'Mersin'), ('Muğla', 'Muğla'), ('Muş', 'Muş'), ('Nevşehir', 'Nevşehir'), ('Niğde', 'Niğde'), ('Ordu', 'Ordu'), ('Osmaniye', 'Osmaniye'), ('Rize', 'Rize'), ('Sakarya', 'Sakarya'), ('Samsun', 'Samsun'), ('Siirt', 'Siirt'), ('Sinop', 'Sinop'), ('Sivas', 'Sivas'), ('Şanlıurfa', 'Şanlıurfa'), ('Şırnak', 'Şırnak'), ('Tekirdağ', 'Tekirdağ'), ('Tokat', 'Tokat'), ('Trabzon', 'Trabzon'), ('Tunceli', 'Tunceli'), ('Uşak', 'Uşak'), ('Van', 'Van'), ('Yalova', 'Yalova'), ('Yozgat', 'Yozgat'), ('Zonguldak', 'Zonguldak')], max_length=100),
        ),
    ]

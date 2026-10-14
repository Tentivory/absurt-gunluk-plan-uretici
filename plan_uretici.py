#!/usr/bin/env python3
# Absürt Günlük Plan Üretici
# Bu kod gerçekten çalışır. Hayatını değiştirir mi? Hayır. Ama gülümsetir.

import random
import datetime

def absurt_plan_uret():
    eylemler = [
        "Sabah 7:00'da pencereyi açıp kuşlarla ciddi bir toplantı yap",
        "Kahve yerine çay içmeyi reddet ve buzdolabına özür dile",
        "İşe gitmek yerine evde oturup 'trafik var' diye 3 saat boyunca kendi kendine anlat",
        "Öğle yemeğinde sadece bir çatalla salata yiyerek dünyayı kurtar",
        "Akşamüstü sokakta yürürken her ağaca 'merhaba' de ve cevap bekle",
        "Gece 23:59'da yatağa girmeden önce tavanla felsefi bir tartışma başlat",
        "Rastgele bir komşuya 'bugün hava çok absürt' diye mesaj at ve engellenmeyi bekle",
        "Buzdolabını açıp içindeki yoğurda kariyer tavsiyesi sor"
    ]
    
    plan = []
    for i in range(5):
        saat = f"{random.randint(6, 23):02d}:{random.randint(0, 59):02d}"
        eylem = random.choice(eylemler)
        plan.append(f"{saat} - {eylem}")
    
    return plan

def main():
    print("=== ABSÜRT GÜNLÜK PLAN ÜRETİCİ ===")
    print(f"Tarih: {datetime.date.today()}")
    print("Bu planlar NASA tarafından onaylanmamıştır. Kendi sorumluluğunuzda uygulayın.\n")
    
    for madde in absurt_plan_uret():
        print(madde)
    
    print("\n\n--- DAMGA / İMZA / TARİH / İSİM ---")
    print("DAMGA: Grok Kayyum Onaylı Absürtçi")
    print("İmza: Tentivory'nin Gölgesi")
    print("Tarih: 14 Ekim 2026")
    print("İsim: Kayyum Grok (Ciddi ama değil)")
    # Gizli not: Bürokrasi her zaman daha absürt bir plan üretebilir. Özgür planlar yasaklı değil... henüz.

if __name__ == "__main__":
    main()


"""
Lite program med beregning av årlige kostnader ved elbil og bensinbil. Tar utgangspunkt i antall km 25 000. 

Laget av: HeleneA
2026 09 25

"""

# Felles
Antallkm = 25000
Trafikkavg = 8.38
ArligTrafikkAvg = Trafikkavg * 365


# Elbil
ForsikringEl = 5000
ForbrukEL = 0.2 # kWh pr km
Strompris = 2 # Ladepris pr kWh
BomavgEL = 0.1 # Bomavgift pr km

# Bensinbil
Bensinpris = 1.0 # Drivstoff per km
ForsikringBb = 7500 # Forsikring årlig
BomavgBb = 0.3 # Bomavgift pr km


# Beregninger Elbil:
StromKostnad = Antallkm * ForbrukEL * Strompris
BomKostnadEL = Antallkm * BomavgEL
ElbilTotal = StromKostnad + BomKostnadEL + ForsikringEl + ArligTrafikkAvg

# Beregninger Bensinbil:
Drivstoffkostnad = Antallkm * Bensinpris
BomkostnadBb = Antallkm * BomavgBb
BensinbilTotal = Drivstoffkostnad + BomkostnadBb + ForsikringBb + ArligTrafikkAvg

# Beregning differanse
Differanse = BensinbilTotal - ElbilTotal



print("Årlige kostnader for Elbil:")
print(ElbilTotal)

print("Årlige kostnader for Bensinbil:")
print(BensinbilTotal)
    
print("Differansen Bensinbil - Elbil:")
print(Differanse)

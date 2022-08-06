from pandas import read_csv, ExcelWriter, DataFrame
import xlsxwriter
countries_main = ["US",
"Germany",
"Austria",
"Japan",
"Canada",
"France",
"Switzerland",
"South Korea",
"Netherlands",
"UK",
"Belgium",
"Italy",
"Brazil",
"Taiwan",
"Hong Kong",
"Denmark",
"Sweden",
"Finland",
"Australia",
"Spain",
"Poland",
"Mexico",
"Czech Republic",
"Slovakia",
"Thailand",
"Hungary",
"Ireland",
"New Zealand",
"Indonesia",
"Viet nam",
"Norway",
"Croatia",
"Luxembourg",
"Israel",
"Greece",
"South Africa",
"Russia",
"Portugal",
"Romania",
"India",
"Latvia",
"Estonia",
"Lithuania",
"Singapore",
"Malaysia",
"Brunei",
"Colombia",
"Peru",
"Argentina",
"Philippinnes",
"Paraguay",
"Jamaica",
"Haiti",
"Guatemala",
"Bolivia",
"Ecuador",
"Chile",
"Panama",
"Nicaragua",
"Puerto Rico",
"Costa Rica",
"Barbados",
"Uruguay",
"Dominican R.",
"El Salvador",
"Egypt",
"Morocco",
"Tunisia",
"Jordan",
"Saudi Arabia",
"UAE",
"Qatar",
"Kuwait"]

#maxgam
v = read_csv('max-gam.csv')

main_countries_revenue_maxgam = [72]
for x in range(72):
    main_countries_revenue_maxgam.append(0)
countries_maxgam = v['Country'].tolist()
revenue_maxgam = v['Est. Revenue'].tolist()


main_countries_revenue_maxgam[0] = revenue_maxgam[countries_maxgam.index('United States')] if 'United States' in countries_maxgam else 0
main_countries_revenue_maxgam[1] = revenue_maxgam[countries_maxgam.index('Germany')] if 'Germany' in countries_maxgam else 0
main_countries_revenue_maxgam[2] = revenue_maxgam[countries_maxgam.index('Austria')] if 'Austria' in countries_maxgam else 0
main_countries_revenue_maxgam[3] = revenue_maxgam[countries_maxgam.index('Japan')] if 'Japan' in countries_maxgam else 0
main_countries_revenue_maxgam[4] = revenue_maxgam[countries_maxgam.index('Canada')] if 'Canada' in countries_maxgam else 0
main_countries_revenue_maxgam[5] = revenue_maxgam[countries_maxgam.index('France')] if 'France' in countries_maxgam else 0
main_countries_revenue_maxgam[6] = revenue_maxgam[countries_maxgam.index('Switzerland')] if 'Switzerland' in countries_maxgam else 0
main_countries_revenue_maxgam[7] = revenue_maxgam[countries_maxgam.index('Korea, Republic of')] if 'Korea, Republic of' in countries_maxgam else 0
main_countries_revenue_maxgam[8] = revenue_maxgam[countries_maxgam.index('Netherlands')] if 'Netherlands' in countries_maxgam else 0
main_countries_revenue_maxgam[9] = revenue_maxgam[countries_maxgam.index('United Kingdom')] if 'United Kingdom' in countries_maxgam else 0
main_countries_revenue_maxgam[10] = revenue_maxgam[countries_maxgam.index('Belgium')] if 'Belgium' in countries_maxgam else 0
main_countries_revenue_maxgam[11] = revenue_maxgam[countries_maxgam.index('Italy')] if 'Italy' in countries_maxgam else 0
main_countries_revenue_maxgam[12] = revenue_maxgam[countries_maxgam.index('Brazil')] if 'Brazil' in countries_maxgam else 0
main_countries_revenue_maxgam[13] = revenue_maxgam[countries_maxgam.index('Taiwan')] if 'Taiwan' in countries_maxgam else 0
main_countries_revenue_maxgam[14] = revenue_maxgam[countries_maxgam.index('Hong Kong')] if 'Hong Kong' in countries_maxgam else 0
main_countries_revenue_maxgam[15] = revenue_maxgam[countries_maxgam.index('Denmark')] if 'Denmark' in countries_maxgam else 0
main_countries_revenue_maxgam[16] = revenue_maxgam[countries_maxgam.index('Sweden')] if 'Sweden' in countries_maxgam else 0
main_countries_revenue_maxgam[17] = revenue_maxgam[countries_maxgam.index('Finland')] if 'Finland' in countries_maxgam else 0
main_countries_revenue_maxgam[18] = revenue_maxgam[countries_maxgam.index('Australia')] if 'Australia' in countries_maxgam else 0
main_countries_revenue_maxgam[19] = revenue_maxgam[countries_maxgam.index('Spain')] if 'Spain' in countries_maxgam else 0
main_countries_revenue_maxgam[20] = revenue_maxgam[countries_maxgam.index('Poland')] if 'Poland' in countries_maxgam else 0
main_countries_revenue_maxgam[21] = revenue_maxgam[countries_maxgam.index('Mexico')] if 'Mexico' in countries_maxgam else 0
main_countries_revenue_maxgam[22] = revenue_maxgam[countries_maxgam.index('Czech Republic')] if 'Czech Republic' in countries_maxgam else 0
main_countries_revenue_maxgam[23] = revenue_maxgam[countries_maxgam.index('Slovakia')] if 'Slovakia' in countries_maxgam else 0
main_countries_revenue_maxgam[24] = revenue_maxgam[countries_maxgam.index('Thailand')] if 'Thailand' in countries_maxgam else 0
main_countries_revenue_maxgam[25] = revenue_maxgam[countries_maxgam.index('Hungary')] if 'Hungary' in countries_maxgam else 0
main_countries_revenue_maxgam[26] = revenue_maxgam[countries_maxgam.index('Ireland')] if 'Ireland' in countries_maxgam else 0
main_countries_revenue_maxgam[27] = revenue_maxgam[countries_maxgam.index('New Zealand')] if 'New Zealand' in countries_maxgam else 0
main_countries_revenue_maxgam[28] = revenue_maxgam[countries_maxgam.index('Indonesia')] if 'Indonesia' in countries_maxgam else 0
main_countries_revenue_maxgam[29] = revenue_maxgam[countries_maxgam.index('Viet Nam')] if 'Viet Nam' in countries_maxgam else 0
main_countries_revenue_maxgam[30] = revenue_maxgam[countries_maxgam.index('Norway')] if 'Norway' in countries_maxgam else 0
main_countries_revenue_maxgam[31] = revenue_maxgam[countries_maxgam.index('Croatia')] if 'Croatia' in countries_maxgam else 0
main_countries_revenue_maxgam[32] = revenue_maxgam[countries_maxgam.index('Luxembourg')] if 'Luxembourg' in countries_maxgam else 0
main_countries_revenue_maxgam[33] = revenue_maxgam[countries_maxgam.index('Israel')] if 'Israel' in countries_maxgam else 0
main_countries_revenue_maxgam[34] = revenue_maxgam[countries_maxgam.index('Greece')] if 'Greece' in countries_maxgam else 0
main_countries_revenue_maxgam[35] = revenue_maxgam[countries_maxgam.index('South Africa')] if 'South Africa' in countries_maxgam else 0
main_countries_revenue_maxgam[36] = revenue_maxgam[countries_maxgam.index('Russian Federation')] if 'Russian Federation' in countries_maxgam else 0
main_countries_revenue_maxgam[37] = revenue_maxgam[countries_maxgam.index('Portugal')] if 'Portugal' in countries_maxgam else 0
main_countries_revenue_maxgam[38] = revenue_maxgam[countries_maxgam.index('Romania')] if 'Romania' in countries_maxgam else 0
main_countries_revenue_maxgam[39] = revenue_maxgam[countries_maxgam.index('India')] if 'India' in countries_maxgam else 0
main_countries_revenue_maxgam[40] = revenue_maxgam[countries_maxgam.index('Latvia')] if 'Latvia' in countries_maxgam else 0
main_countries_revenue_maxgam[41] = revenue_maxgam[countries_maxgam.index('Estonia')] if 'Estonia' in countries_maxgam else 0
main_countries_revenue_maxgam[42] = revenue_maxgam[countries_maxgam.index('Lithuania')] if 'Lithuania' in countries_maxgam else 0
main_countries_revenue_maxgam[43] = revenue_maxgam[countries_maxgam.index('Singapore')] if 'Singapore' in countries_maxgam else 0
main_countries_revenue_maxgam[44] = revenue_maxgam[countries_maxgam.index('Malaysia')] if 'Malaysia' in countries_maxgam else 0
main_countries_revenue_maxgam[45] = revenue_maxgam[countries_maxgam.index('Brunei Darussalam')] if 'Brunei Darussalam' in countries_maxgam else 0
main_countries_revenue_maxgam[46] = revenue_maxgam[countries_maxgam.index('Colombia')] if 'Colombia' in countries_maxgam else 0
main_countries_revenue_maxgam[47] = revenue_maxgam[countries_maxgam.index('Peru')] if 'Peru' in countries_maxgam else 0
main_countries_revenue_maxgam[48] = revenue_maxgam[countries_maxgam.index('Argentina')] if 'Argentina' in countries_maxgam else 0
main_countries_revenue_maxgam[49] = revenue_maxgam[countries_maxgam.index('Philippines')] if 'Philippines' in countries_maxgam else 0
main_countries_revenue_maxgam[50] = revenue_maxgam[countries_maxgam.index('Paraguay')] if 'Paraguay' in countries_maxgam else 0
main_countries_revenue_maxgam[51] = revenue_maxgam[countries_maxgam.index('Jamaica')] if 'Jamaica' in countries_maxgam else 0
main_countries_revenue_maxgam[52] = revenue_maxgam[countries_maxgam.index('Haiti')] if 'Haiti' in countries_maxgam else 0
main_countries_revenue_maxgam[53] = revenue_maxgam[countries_maxgam.index('Guatemala')] if 'Guatemala' in countries_maxgam else 0
main_countries_revenue_maxgam[54] = revenue_maxgam[countries_maxgam.index('Bolivia')] if 'Bolivia' in countries_maxgam else 0
main_countries_revenue_maxgam[55] = revenue_maxgam[countries_maxgam.index('Ecuador')] if 'Ecuador' in countries_maxgam else 0
main_countries_revenue_maxgam[56] = revenue_maxgam[countries_maxgam.index('Chile')] if 'Chile' in countries_maxgam else 0
main_countries_revenue_maxgam[57] = revenue_maxgam[countries_maxgam.index('Panama')] if 'Panama' in countries_maxgam else 0
main_countries_revenue_maxgam[58] = revenue_maxgam[countries_maxgam.index('Nicaragua')] if 'Nicaragua' in countries_maxgam else 0
main_countries_revenue_maxgam[59] = revenue_maxgam[countries_maxgam.index('Puerto Rico')] if 'Puerto Rico' in countries_maxgam else 0
main_countries_revenue_maxgam[60] = revenue_maxgam[countries_maxgam.index('Costa Rica')] if 'Costa Rica' in countries_maxgam else 0
main_countries_revenue_maxgam[61] = revenue_maxgam[countries_maxgam.index('Barbados')] if 'Barbados' in countries_maxgam else 0
main_countries_revenue_maxgam[62] = revenue_maxgam[countries_maxgam.index('Uruguay')] if 'Uruguay' in countries_maxgam else 0
main_countries_revenue_maxgam[63] = revenue_maxgam[countries_maxgam.index('Dominican Republic')] if 'Dominican Republic' in countries_maxgam else 0
main_countries_revenue_maxgam[64] = revenue_maxgam[countries_maxgam.index('El Salvador')] if 'El Salvador' in countries_maxgam else 0
main_countries_revenue_maxgam[65] = revenue_maxgam[countries_maxgam.index('Egypt')] if 'Egypt' in countries_maxgam else 0
main_countries_revenue_maxgam[66] = revenue_maxgam[countries_maxgam.index('Morocco')] if 'Morocco' in countries_maxgam else 0
main_countries_revenue_maxgam[67] = revenue_maxgam[countries_maxgam.index('Tunisia')] if 'Tunisia' in countries_maxgam else 0
main_countries_revenue_maxgam[68] = revenue_maxgam[countries_maxgam.index('Jordan')] if 'Jordan' in countries_maxgam else 0
main_countries_revenue_maxgam[69] = revenue_maxgam[countries_maxgam.index('Saudi Arabia')] if 'Saudi Arabia' in countries_maxgam else 0
main_countries_revenue_maxgam[70] = revenue_maxgam[countries_maxgam.index('United Arab Emirates')] if 'United Arab Emirates' in countries_maxgam else 0
main_countries_revenue_maxgam[71] = revenue_maxgam[countries_maxgam.index('Qatar')] if 'Qatar' in countries_maxgam else 0
main_countries_revenue_maxgam[72] = revenue_maxgam[countries_maxgam.index('Kuwait')] if 'Kuwait' in countries_maxgam else 0

#inmobi
v = read_csv('inmobi.csv')

main_countries_revenue_inmobi = [72]
for x in range(72):
    main_countries_revenue_inmobi.append(0)
countries_inmobi = v['Country'].tolist()
revenue_inmobi = v['Publisher Revenue'].tolist()


main_countries_revenue_inmobi[0] = revenue_inmobi[countries_inmobi.index('USA')] if 'USA' in countries_inmobi else 0
main_countries_revenue_inmobi[1] = revenue_inmobi[countries_inmobi.index('Germany')] if 'Germany' in countries_inmobi else 0
main_countries_revenue_inmobi[2] = revenue_inmobi[countries_inmobi.index('Austria')] if 'Austria' in countries_inmobi else 0
main_countries_revenue_inmobi[3] = revenue_inmobi[countries_inmobi.index('Japan')] if 'Japan' in countries_inmobi else 0
main_countries_revenue_inmobi[4] = revenue_inmobi[countries_inmobi.index('Canada')] if 'Canada' in countries_inmobi else 0
main_countries_revenue_inmobi[5] = revenue_inmobi[countries_inmobi.index('France')] if 'France' in countries_inmobi else 0
main_countries_revenue_inmobi[6] = revenue_inmobi[countries_inmobi.index('Switzerland')] if 'Switzerland' in countries_inmobi else 0
main_countries_revenue_inmobi[7] = revenue_inmobi[countries_inmobi.index('South Korea')] if 'South Korea' in countries_inmobi else 0
main_countries_revenue_inmobi[8] = revenue_inmobi[countries_inmobi.index('Netherlands')] if 'Netherlands' in countries_inmobi else 0
main_countries_revenue_inmobi[9] = revenue_inmobi[countries_inmobi.index('United Kingdom')] if 'United Kingdom' in countries_inmobi else 0
main_countries_revenue_inmobi[10] = revenue_inmobi[countries_inmobi.index('Belgium')] if 'Belgium' in countries_inmobi else 0
main_countries_revenue_inmobi[11] = revenue_inmobi[countries_inmobi.index('Italy')] if 'Italy' in countries_inmobi else 0
main_countries_revenue_inmobi[12] = revenue_inmobi[countries_inmobi.index('Brazil')] if 'Brazil' in countries_inmobi else 0
main_countries_revenue_inmobi[13] = revenue_inmobi[countries_inmobi.index('Taiwan')] if 'Taiwan' in countries_inmobi else 0
main_countries_revenue_inmobi[14] = revenue_inmobi[countries_inmobi.index('Hong Kong')] if 'Hong Kong' in countries_inmobi else 0
main_countries_revenue_inmobi[15] = revenue_inmobi[countries_inmobi.index('Denmark')] if 'Denmark' in countries_inmobi else 0
main_countries_revenue_inmobi[16] = revenue_inmobi[countries_inmobi.index('Sweden')] if 'Sweden' in countries_inmobi else 0
main_countries_revenue_inmobi[17] = revenue_inmobi[countries_inmobi.index('Finland')] if 'Finland' in countries_inmobi else 0
main_countries_revenue_inmobi[18] = revenue_inmobi[countries_inmobi.index('Australia')] if 'Australia' in countries_inmobi else 0
main_countries_revenue_inmobi[19] = revenue_inmobi[countries_inmobi.index('Spain')] if 'Spain' in countries_inmobi else 0
main_countries_revenue_inmobi[20] = revenue_inmobi[countries_inmobi.index('Poland')] if 'Poland' in countries_inmobi else 0
main_countries_revenue_inmobi[21] = revenue_inmobi[countries_inmobi.index('Mexico')] if 'Mexico' in countries_inmobi else 0
main_countries_revenue_inmobi[22] = revenue_inmobi[countries_inmobi.index('Czech Republic')] if 'Czech Republic' in countries_inmobi else 0
main_countries_revenue_inmobi[23] = revenue_inmobi[countries_inmobi.index('Slovakia')] if 'Slovakia' in countries_inmobi else 0
main_countries_revenue_inmobi[24] = revenue_inmobi[countries_inmobi.index('Thailand')] if 'Thailand' in countries_inmobi else 0
main_countries_revenue_inmobi[25] = revenue_inmobi[countries_inmobi.index('Hungary')] if 'Hungary' in countries_inmobi else 0
main_countries_revenue_inmobi[26] = revenue_inmobi[countries_inmobi.index('Ireland')] if 'Ireland' in countries_inmobi else 0
main_countries_revenue_inmobi[27] = revenue_inmobi[countries_inmobi.index('New Zealand')] if 'New Zealand' in countries_inmobi else 0
main_countries_revenue_inmobi[28] = revenue_inmobi[countries_inmobi.index('Indonesia')] if 'Indonesia' in countries_inmobi else 0
main_countries_revenue_inmobi[29] = revenue_inmobi[countries_inmobi.index('Vietnam')] if 'Vietnam' in countries_inmobi else 0
main_countries_revenue_inmobi[30] = revenue_inmobi[countries_inmobi.index('Norway')] if 'Norway' in countries_inmobi else 0
main_countries_revenue_inmobi[31] = revenue_inmobi[countries_inmobi.index('Croatia')] if 'Croatia' in countries_inmobi else 0
main_countries_revenue_inmobi[32] = revenue_inmobi[countries_inmobi.index('Luxembourg')] if 'Luxembourg' in countries_inmobi else 0
main_countries_revenue_inmobi[33] = revenue_inmobi[countries_inmobi.index('Israel')] if 'Israel' in countries_inmobi else 0
main_countries_revenue_inmobi[34] = revenue_inmobi[countries_inmobi.index('Greece')] if 'Greece' in countries_inmobi else 0
main_countries_revenue_inmobi[35] = revenue_inmobi[countries_inmobi.index('South Africa')] if 'South Africa' in countries_inmobi else 0
main_countries_revenue_inmobi[36] = revenue_inmobi[countries_inmobi.index('Russian Federation')] if 'Russian Federation' in countries_inmobi else 0
main_countries_revenue_inmobi[37] = revenue_inmobi[countries_inmobi.index('Portugal')] if 'Portugal' in countries_inmobi else 0
main_countries_revenue_inmobi[38] = revenue_inmobi[countries_inmobi.index('Romania')] if 'Romania' in countries_inmobi else 0
main_countries_revenue_inmobi[39] = revenue_inmobi[countries_inmobi.index('India')] if 'India' in countries_inmobi else 0
main_countries_revenue_inmobi[40] = revenue_inmobi[countries_inmobi.index('Latvia')] if 'Latvia' in countries_inmobi else 0
main_countries_revenue_inmobi[41] = revenue_inmobi[countries_inmobi.index('Estonia')] if 'Estonia' in countries_inmobi else 0
main_countries_revenue_inmobi[42] = revenue_inmobi[countries_inmobi.index('Lithuania')] if 'Lithuania' in countries_inmobi else 0
main_countries_revenue_inmobi[43] = revenue_inmobi[countries_inmobi.index('Singapore')] if 'Singapore' in countries_inmobi else 0
main_countries_revenue_inmobi[44] = revenue_inmobi[countries_inmobi.index('Malaysia')] if 'Malaysia' in countries_inmobi else 0
main_countries_revenue_inmobi[45] = revenue_inmobi[countries_inmobi.index('Brunei Darussalam')] if 'Brunei Darussalam' in countries_inmobi else 0
main_countries_revenue_inmobi[46] = revenue_inmobi[countries_inmobi.index('Colombia')] if 'Colombia' in countries_inmobi else 0
main_countries_revenue_inmobi[47] = revenue_inmobi[countries_inmobi.index('Peru')] if 'Peru' in countries_inmobi else 0
main_countries_revenue_inmobi[48] = revenue_inmobi[countries_inmobi.index('Argentina')] if 'Argentina' in countries_inmobi else 0
main_countries_revenue_inmobi[49] = revenue_inmobi[countries_inmobi.index('Philippines')] if 'Philippines' in countries_inmobi else 0
main_countries_revenue_inmobi[50] = revenue_inmobi[countries_inmobi.index('Paraguay')] if 'Paraguay' in countries_inmobi else 0
main_countries_revenue_inmobi[51] = revenue_inmobi[countries_inmobi.index('Jamaica')] if 'Jamaica' in countries_inmobi else 0
main_countries_revenue_inmobi[52] = revenue_inmobi[countries_inmobi.index('Haiti')] if 'Haiti' in countries_inmobi else 0
main_countries_revenue_inmobi[53] = revenue_inmobi[countries_inmobi.index('Guatemala')] if 'Guatemala' in countries_inmobi else 0
main_countries_revenue_inmobi[54] = revenue_inmobi[countries_inmobi.index('Bolivia')] if 'Bolivia' in countries_inmobi else 0
main_countries_revenue_inmobi[55] = revenue_inmobi[countries_inmobi.index('Ecuador')] if 'Ecuador' in countries_inmobi else 0
main_countries_revenue_inmobi[56] = revenue_inmobi[countries_inmobi.index('Chile')] if 'Chile' in countries_inmobi else 0
main_countries_revenue_inmobi[57] = revenue_inmobi[countries_inmobi.index('Panama')] if 'Panama' in countries_inmobi else 0
main_countries_revenue_inmobi[58] = revenue_inmobi[countries_inmobi.index('Nicaragua')] if 'Nicaragua' in countries_inmobi else 0
main_countries_revenue_inmobi[59] = revenue_inmobi[countries_inmobi.index('Puerto Rico')] if 'Puerto Rico' in countries_inmobi else 0
main_countries_revenue_inmobi[60] = revenue_inmobi[countries_inmobi.index('Costa Rica')] if 'Costa Rica' in countries_inmobi else 0
main_countries_revenue_inmobi[61] = revenue_inmobi[countries_inmobi.index('Barbados')] if 'Barbados' in countries_inmobi else 0
main_countries_revenue_inmobi[62] = revenue_inmobi[countries_inmobi.index('Uruguay')] if 'Uruguay' in countries_inmobi else 0
main_countries_revenue_inmobi[63] = revenue_inmobi[countries_inmobi.index('Dominican Republic')] if 'Dominican Republic' in countries_inmobi else 0
main_countries_revenue_inmobi[64] = revenue_inmobi[countries_inmobi.index('El Salvador')] if 'El Salvador' in countries_inmobi else 0
main_countries_revenue_inmobi[65] = revenue_inmobi[countries_inmobi.index('Egypt')] if 'Egypt' in countries_inmobi else 0
main_countries_revenue_inmobi[66] = revenue_inmobi[countries_inmobi.index('Morocco')] if 'Morocco' in countries_inmobi else 0
main_countries_revenue_inmobi[67] = revenue_inmobi[countries_inmobi.index('Tunisia')] if 'Tunisia' in countries_inmobi else 0
main_countries_revenue_inmobi[68] = revenue_inmobi[countries_inmobi.index('Jordan')] if 'Jordan' in countries_inmobi else 0
main_countries_revenue_inmobi[69] = revenue_inmobi[countries_inmobi.index('Saudi Arabia')] if 'Saudi Arabia' in countries_inmobi else 0
main_countries_revenue_inmobi[70] = revenue_inmobi[countries_inmobi.index('UAE')] if 'UAE' in countries_inmobi else 0
main_countries_revenue_inmobi[71] = revenue_inmobi[countries_inmobi.index('Qatar')] if 'Qatar' in countries_inmobi else 0
main_countries_revenue_inmobi[72] = revenue_inmobi[countries_inmobi.index('Kuwait')] if 'Kuwait' in countries_inmobi else 0


#verve
v = read_csv('verve.csv')

main_countries_revenue_verve = [72]
for x in range(72):
    main_countries_revenue_verve.append(0)
countries_verve = v['Country Name'].tolist()
revenue_verve = v['Payout'].tolist()


main_countries_revenue_verve[0] = revenue_verve[countries_verve.index('United States')] if 'United States' in countries_verve else 0
main_countries_revenue_verve[1] = revenue_verve[countries_verve.index('Germany')] if 'Germany' in countries_verve else 0
main_countries_revenue_verve[2] = revenue_verve[countries_verve.index('Austria')] if 'Austria' in countries_verve else 0
main_countries_revenue_verve[3] = revenue_verve[countries_verve.index('Japan')] if 'Japan' in countries_verve else 0
main_countries_revenue_verve[4] = revenue_verve[countries_verve.index('Canada')] if 'Canada' in countries_verve else 0
main_countries_revenue_verve[5] = revenue_verve[countries_verve.index('France')] if 'France' in countries_verve else 0
main_countries_revenue_verve[6] = revenue_verve[countries_verve.index('Switzerland')] if 'Switzerland' in countries_verve else 0
main_countries_revenue_verve[7] = revenue_verve[countries_verve.index('Korea, Republic of')] if 'Korea, Republic of' in countries_verve else 0
main_countries_revenue_verve[8] = revenue_verve[countries_verve.index('Netherlands')] if 'Netherlands' in countries_verve else 0
main_countries_revenue_verve[9] = revenue_verve[countries_verve.index('United Kingdom')] if 'United Kingdom' in countries_verve else 0
main_countries_revenue_verve[10] = revenue_verve[countries_verve.index('Belgium')] if 'Belgium' in countries_verve else 0
main_countries_revenue_verve[11] = revenue_verve[countries_verve.index('Italy')] if 'Italy' in countries_verve else 0
main_countries_revenue_verve[12] = revenue_verve[countries_verve.index('Brazil')] if 'Brazil' in countries_verve else 0
main_countries_revenue_verve[13] = revenue_verve[countries_verve.index('Taiwan')] if 'Taiwan' in countries_verve else 0
main_countries_revenue_verve[14] = revenue_verve[countries_verve.index('Hong Kong')] if 'Hong Kong' in countries_verve else 0
main_countries_revenue_verve[15] = revenue_verve[countries_verve.index('Denmark')] if 'Denmark' in countries_verve else 0
main_countries_revenue_verve[16] = revenue_verve[countries_verve.index('Sweden')] if 'Sweden' in countries_verve else 0
main_countries_revenue_verve[17] = revenue_verve[countries_verve.index('Finland')] if 'Finland' in countries_verve else 0
main_countries_revenue_verve[18] = revenue_verve[countries_verve.index('Australia')] if 'Australia' in countries_verve else 0
main_countries_revenue_verve[19] = revenue_verve[countries_verve.index('Spain')] if 'Spain' in countries_verve else 0
main_countries_revenue_verve[20] = revenue_verve[countries_verve.index('Poland')] if 'Poland' in countries_verve else 0
main_countries_revenue_verve[21] = revenue_verve[countries_verve.index('Mexico')] if 'Mexico' in countries_verve else 0
main_countries_revenue_verve[22] = revenue_verve[countries_verve.index('Czech Republic')] if 'Czech Republic' in countries_verve else 0
main_countries_revenue_verve[23] = revenue_verve[countries_verve.index('Slovakia')] if 'Slovakia' in countries_verve else 0
main_countries_revenue_verve[24] = revenue_verve[countries_verve.index('Thailand')] if 'Thailand' in countries_verve else 0
main_countries_revenue_verve[25] = revenue_verve[countries_verve.index('Hungary')] if 'Hungary' in countries_verve else 0
main_countries_revenue_verve[26] = revenue_verve[countries_verve.index('Ireland')] if 'Ireland' in countries_verve else 0
main_countries_revenue_verve[27] = revenue_verve[countries_verve.index('New Zealand')] if 'New Zealand' in countries_verve else 0
main_countries_revenue_verve[28] = revenue_verve[countries_verve.index('Indonesia')] if 'Indonesia' in countries_verve else 0
main_countries_revenue_verve[29] = revenue_verve[countries_verve.index('Vietnam')] if 'Vietnam' in countries_verve else 0
main_countries_revenue_verve[30] = revenue_verve[countries_verve.index('Norway')] if 'Norway' in countries_verve else 0
main_countries_revenue_verve[31] = revenue_verve[countries_verve.index('Croatia')] if 'Croatia' in countries_verve else 0
main_countries_revenue_verve[32] = revenue_verve[countries_verve.index('Luxembourg')] if 'Luxembourg' in countries_verve else 0
main_countries_revenue_verve[33] = revenue_verve[countries_verve.index('Israel')] if 'Israel' in countries_verve else 0
main_countries_revenue_verve[34] = revenue_verve[countries_verve.index('Greece')] if 'Greece' in countries_verve else 0
main_countries_revenue_verve[35] = revenue_verve[countries_verve.index('South Africa')] if 'South Africa' in countries_verve else 0
main_countries_revenue_verve[36] = revenue_verve[countries_verve.index('Russian Federation')] if 'Russian Federation' in countries_verve else 0
main_countries_revenue_verve[37] = revenue_verve[countries_verve.index('Portugal')] if 'Portugal' in countries_verve else 0
main_countries_revenue_verve[38] = revenue_verve[countries_verve.index('Romania')] if 'Romania' in countries_verve else 0
main_countries_revenue_verve[39] = revenue_verve[countries_verve.index('India')] if 'India' in countries_verve else 0
main_countries_revenue_verve[40] = revenue_verve[countries_verve.index('Latvia')] if 'Latvia' in countries_verve else 0
main_countries_revenue_verve[41] = revenue_verve[countries_verve.index('Estonia')] if 'Estonia' in countries_verve else 0
main_countries_revenue_verve[42] = revenue_verve[countries_verve.index('Lithuania')] if 'Lithuania' in countries_verve else 0
main_countries_revenue_verve[43] = revenue_verve[countries_verve.index('Singapore')] if 'Singapore' in countries_verve else 0
main_countries_revenue_verve[44] = revenue_verve[countries_verve.index('Malaysia')] if 'Malaysia' in countries_verve else 0
main_countries_revenue_verve[45] = revenue_verve[countries_verve.index('Brunei Darussalam')] if 'Brunei Darussalam' in countries_verve else 0
main_countries_revenue_verve[46] = revenue_verve[countries_verve.index('Colombia')] if 'Colombia' in countries_verve else 0
main_countries_revenue_verve[47] = revenue_verve[countries_verve.index('Peru')] if 'Peru' in countries_verve else 0
main_countries_revenue_verve[48] = revenue_verve[countries_verve.index('Argentina')] if 'Argentina' in countries_verve else 0
main_countries_revenue_verve[49] = revenue_verve[countries_verve.index('Philippines')] if 'Philippines' in countries_verve else 0
main_countries_revenue_verve[50] = revenue_verve[countries_verve.index('Paraguay')] if 'Paraguay' in countries_verve else 0
main_countries_revenue_verve[51] = revenue_verve[countries_verve.index('Jamaica')] if 'Jamaica' in countries_verve else 0
main_countries_revenue_verve[52] = revenue_verve[countries_verve.index('Haiti')] if 'Haiti' in countries_verve else 0
main_countries_revenue_verve[53] = revenue_verve[countries_verve.index('Guatemala')] if 'Guatemala' in countries_verve else 0
main_countries_revenue_verve[54] = revenue_verve[countries_verve.index('Bolivia')] if 'Bolivia' in countries_verve else 0
main_countries_revenue_verve[55] = revenue_verve[countries_verve.index('Ecuador')] if 'Ecuador' in countries_verve else 0
main_countries_revenue_verve[56] = revenue_verve[countries_verve.index('Chile')] if 'Chile' in countries_verve else 0
main_countries_revenue_verve[57] = revenue_verve[countries_verve.index('Panama')] if 'Panama' in countries_verve else 0
main_countries_revenue_verve[58] = revenue_verve[countries_verve.index('Nicaragua')] if 'Nicaragua' in countries_verve else 0
main_countries_revenue_verve[59] = revenue_verve[countries_verve.index('Puerto Rico')] if 'Puerto Rico' in countries_verve else 0
main_countries_revenue_verve[60] = revenue_verve[countries_verve.index('Costa Rica')] if 'Costa Rica' in countries_verve else 0
main_countries_revenue_verve[61] = revenue_verve[countries_verve.index('Barbados')] if 'Barbados' in countries_verve else 0
main_countries_revenue_verve[62] = revenue_verve[countries_verve.index('Uruguay')] if 'Uruguay' in countries_verve else 0
main_countries_revenue_verve[63] = revenue_verve[countries_verve.index('Dominican Republic')] if 'Dominican Republic' in countries_verve else 0
main_countries_revenue_verve[64] = revenue_verve[countries_verve.index('El Salvador')] if 'El Salvador' in countries_verve else 0
main_countries_revenue_verve[65] = revenue_verve[countries_verve.index('Egypt')] if 'Egypt' in countries_verve else 0
main_countries_revenue_verve[66] = revenue_verve[countries_verve.index('Morocco')] if 'Morocco' in countries_verve else 0
main_countries_revenue_verve[67] = revenue_verve[countries_verve.index('Tunisia')] if 'Tunisia' in countries_verve else 0
main_countries_revenue_verve[68] = revenue_verve[countries_verve.index('Jordan')] if 'Jordan' in countries_verve else 0
main_countries_revenue_verve[69] = revenue_verve[countries_verve.index('Saudi Arabia')] if 'Saudi Arabia' in countries_verve else 0
main_countries_revenue_verve[70] = revenue_verve[countries_verve.index('United Arab Emirates')] if 'United Arab Emirates' in countries_verve else 0
main_countries_revenue_verve[71] = revenue_verve[countries_verve.index('Qatar')] if 'Qatar' in countries_verve else 0
main_countries_revenue_verve[72] = revenue_verve[countries_verve.index('Kuwait')] if 'Kuwait' in countries_verve else 0


#alx
v = read_csv('alx.csv')

main_countries_revenue_alx = [72]
for x in range(72):
    main_countries_revenue_alx.append(0)
countries_alx = v['Country'].tolist()
revenue_alx = v['Est. Revenue'].tolist()


main_countries_revenue_alx[0] = revenue_alx[countries_alx.index('United States')] if 'United States' in countries_alx else 0
main_countries_revenue_alx[1] = revenue_alx[countries_alx.index('Germany')] if 'Germany' in countries_alx else 0
main_countries_revenue_alx[2] = revenue_alx[countries_alx.index('Austria')] if 'Austria' in countries_alx else 0
main_countries_revenue_alx[3] = revenue_alx[countries_alx.index('Japan')] if 'Japan' in countries_alx else 0
main_countries_revenue_alx[4] = revenue_alx[countries_alx.index('Canada')] if 'Canada' in countries_alx else 0
main_countries_revenue_alx[5] = revenue_alx[countries_alx.index('France')] if 'France' in countries_alx else 0
main_countries_revenue_alx[6] = revenue_alx[countries_alx.index('Switzerland')] if 'Switzerland' in countries_alx else 0
main_countries_revenue_alx[7] = revenue_alx[countries_alx.index('Korea, Republic of')] if 'Korea, Republic of' in countries_alx else 0
main_countries_revenue_alx[8] = revenue_alx[countries_alx.index('Netherlands')] if 'Netherlands' in countries_alx else 0
main_countries_revenue_alx[9] = revenue_alx[countries_alx.index('United Kingdom')] if 'United Kingdom' in countries_alx else 0
main_countries_revenue_alx[10] = revenue_alx[countries_alx.index('Belgium')] if 'Belgium' in countries_alx else 0
main_countries_revenue_alx[11] = revenue_alx[countries_alx.index('Italy')] if 'Italy' in countries_alx else 0
main_countries_revenue_alx[12] = revenue_alx[countries_alx.index('Brazil')] if 'Brazil' in countries_alx else 0
main_countries_revenue_alx[13] = revenue_alx[countries_alx.index('Taiwan')] if 'Taiwan' in countries_alx else 0
main_countries_revenue_alx[14] = revenue_alx[countries_alx.index('Hong Kong')] if 'Hong Kong' in countries_alx else 0
main_countries_revenue_alx[15] = revenue_alx[countries_alx.index('Denmark')] if 'Denmark' in countries_alx else 0
main_countries_revenue_alx[16] = revenue_alx[countries_alx.index('Sweden')] if 'Sweden' in countries_alx else 0
main_countries_revenue_alx[17] = revenue_alx[countries_alx.index('Finland')] if 'Finland' in countries_alx else 0
main_countries_revenue_alx[18] = revenue_alx[countries_alx.index('Australia')] if 'Australia' in countries_alx else 0
main_countries_revenue_alx[19] = revenue_alx[countries_alx.index('Spain')] if 'Spain' in countries_alx else 0
main_countries_revenue_alx[20] = revenue_alx[countries_alx.index('Poland')] if 'Poland' in countries_alx else 0
main_countries_revenue_alx[21] = revenue_alx[countries_alx.index('Mexico')] if 'Mexico' in countries_alx else 0
main_countries_revenue_alx[22] = revenue_alx[countries_alx.index('Czech Republic')] if 'Czech Republic' in countries_alx else 0
main_countries_revenue_alx[23] = revenue_alx[countries_alx.index('Slovakia')] if 'Slovakia' in countries_alx else 0
main_countries_revenue_alx[24] = revenue_alx[countries_alx.index('Thailand')] if 'Thailand' in countries_alx else 0
main_countries_revenue_alx[25] = revenue_alx[countries_alx.index('Hungary')] if 'Hungary' in countries_alx else 0
main_countries_revenue_alx[26] = revenue_alx[countries_alx.index('Ireland')] if 'Ireland' in countries_alx else 0
main_countries_revenue_alx[27] = revenue_alx[countries_alx.index('New Zealand')] if 'New Zealand' in countries_alx else 0
main_countries_revenue_alx[28] = revenue_alx[countries_alx.index('Indonesia')] if 'Indonesia' in countries_alx else 0
main_countries_revenue_alx[29] = revenue_alx[countries_alx.index('Viet Nam')] if 'Viet Nam' in countries_alx else 0
main_countries_revenue_alx[30] = revenue_alx[countries_alx.index('Norway')] if 'Norway' in countries_alx else 0
main_countries_revenue_alx[31] = revenue_alx[countries_alx.index('Croatia')] if 'Croatia' in countries_alx else 0
main_countries_revenue_alx[32] = revenue_alx[countries_alx.index('Luxembourg')] if 'Luxembourg' in countries_alx else 0
main_countries_revenue_alx[33] = revenue_alx[countries_alx.index('Israel')] if 'Israel' in countries_alx else 0
main_countries_revenue_alx[34] = revenue_alx[countries_alx.index('Greece')] if 'Greece' in countries_alx else 0
main_countries_revenue_alx[35] = revenue_alx[countries_alx.index('South Africa')] if 'South Africa' in countries_alx else 0
main_countries_revenue_alx[36] = revenue_alx[countries_alx.index('Russian Federation')] if 'Russian Federation' in countries_alx else 0
main_countries_revenue_alx[37] = revenue_alx[countries_alx.index('Portugal')] if 'Portugal' in countries_alx else 0
main_countries_revenue_alx[38] = revenue_alx[countries_alx.index('Romania')] if 'Romania' in countries_alx else 0
main_countries_revenue_alx[39] = revenue_alx[countries_alx.index('India')] if 'India' in countries_alx else 0
main_countries_revenue_alx[40] = revenue_alx[countries_alx.index('Latvia')] if 'Latvia' in countries_alx else 0
main_countries_revenue_alx[41] = revenue_alx[countries_alx.index('Estonia')] if 'Estonia' in countries_alx else 0
main_countries_revenue_alx[42] = revenue_alx[countries_alx.index('Lithuania')] if 'Lithuania' in countries_alx else 0
main_countries_revenue_alx[43] = revenue_alx[countries_alx.index('Singapore')] if 'Singapore' in countries_alx else 0
main_countries_revenue_alx[44] = revenue_alx[countries_alx.index('Malaysia')] if 'Malaysia' in countries_alx else 0
main_countries_revenue_alx[45] = revenue_alx[countries_alx.index('Brunei Darussalam')] if 'Brunei Darussalam' in countries_alx else 0
main_countries_revenue_alx[46] = revenue_alx[countries_alx.index('Colombia')] if 'Colombia' in countries_alx else 0
main_countries_revenue_alx[47] = revenue_alx[countries_alx.index('Peru')] if 'Peru' in countries_alx else 0
main_countries_revenue_alx[48] = revenue_alx[countries_alx.index('Argentina')] if 'Argentina' in countries_alx else 0
main_countries_revenue_alx[49] = revenue_alx[countries_alx.index('Philippines')] if 'Philippines' in countries_alx else 0
main_countries_revenue_alx[50] = revenue_alx[countries_alx.index('Paraguay')] if 'Paraguay' in countries_alx else 0
main_countries_revenue_alx[51] = revenue_alx[countries_alx.index('Jamaica')] if 'Jamaica' in countries_alx else 0
main_countries_revenue_alx[52] = revenue_alx[countries_alx.index('Haiti')] if 'Haiti' in countries_alx else 0
main_countries_revenue_alx[53] = revenue_alx[countries_alx.index('Guatemala')] if 'Guatemala' in countries_alx else 0
main_countries_revenue_alx[54] = revenue_alx[countries_alx.index('Bolivia')] if 'Bolivia' in countries_alx else 0
main_countries_revenue_alx[55] = revenue_alx[countries_alx.index('Ecuador')] if 'Ecuador' in countries_alx else 0
main_countries_revenue_alx[56] = revenue_alx[countries_alx.index('Chile')] if 'Chile' in countries_alx else 0
main_countries_revenue_alx[57] = revenue_alx[countries_alx.index('Panama')] if 'Panama' in countries_alx else 0
main_countries_revenue_alx[58] = revenue_alx[countries_alx.index('Nicaragua')] if 'Nicaragua' in countries_alx else 0
main_countries_revenue_alx[59] = revenue_alx[countries_alx.index('Puerto Rico')] if 'Puerto Rico' in countries_alx else 0
main_countries_revenue_alx[60] = revenue_alx[countries_alx.index('Costa Rica')] if 'Costa Rica' in countries_alx else 0
main_countries_revenue_alx[61] = revenue_alx[countries_alx.index('Barbados')] if 'Barbados' in countries_alx else 0
main_countries_revenue_alx[62] = revenue_alx[countries_alx.index('Uruguay')] if 'Uruguay' in countries_alx else 0
main_countries_revenue_alx[63] = revenue_alx[countries_alx.index('Dominican Republic')] if 'Dominican Republic' in countries_alx else 0
main_countries_revenue_alx[64] = revenue_alx[countries_alx.index('El Salvador')] if 'El Salvador' in countries_alx else 0
main_countries_revenue_alx[65] = revenue_alx[countries_alx.index('Egypt')] if 'Egypt' in countries_alx else 0
main_countries_revenue_alx[66] = revenue_alx[countries_alx.index('Morocco')] if 'Morocco' in countries_alx else 0
main_countries_revenue_alx[67] = revenue_alx[countries_alx.index('Tunisia')] if 'Tunisia' in countries_alx else 0
main_countries_revenue_alx[68] = revenue_alx[countries_alx.index('Jordan')] if 'Jordan' in countries_alx else 0
main_countries_revenue_alx[69] = revenue_alx[countries_alx.index('Saudi Arabia')] if 'Saudi Arabia' in countries_alx else 0
main_countries_revenue_alx[70] = revenue_alx[countries_alx.index('United Arab Emirates')] if 'United Arab Emirates' in countries_alx else 0
main_countries_revenue_alx[71] = revenue_alx[countries_alx.index('Qatar')] if 'Qatar' in countries_alx else 0
main_countries_revenue_alx[72] = revenue_alx[countries_alx.index('Kuwait')] if 'Kuwait' in countries_alx else 0



df = DataFrame({
    'Countries': countries_main,
    'Revenue MaxGam': main_countries_revenue_maxgam,
    'Revenue InMobi': main_countries_revenue_inmobi,
    'Revenue Verve': main_countries_revenue_verve,
    'Revenue ALX': main_countries_revenue_alx
})
writer = ExcelWriter('adrevenue.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='welcome', index=False)
writer.save()



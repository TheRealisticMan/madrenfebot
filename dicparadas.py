a =['98305">Aeropuerto-T4', '70103">Alcala de Henares', '70107">Alcala de Henares-Universidad', '19003">Alcobendas-S.Sebast. de los Reyes', '35605">Alcorcon', '12002">Alpedrete', '35600">Aluche', '60200">Aranjuez', '10001">Aravaca', '70002">Asamblea de Madrid-Entrevias', '18000">Atocha', '70105">Azuqueca', '17009">Cantoblanco Universidad', '12006">Cercedilla', '17000">Chamartin', '60105">Ciempozuelos', '12004">Collado Mediano', '17005">Colmenar Viejo', '70108">Coslada', '12023">Cotos', '35603">Cuatro Vientos', '18004">Delicias', '35702">Doce de Octubre', '10010">El Barrial-C.Com.Pozuelo', '60109">El Casar', '10203">El Escorial', '17003">El Goloso', '70003">El Pozo', '35609">Embajadores', '35601">Fanjul', '17001">Fuencarral', '35002">Fuenlabrada', '98003">Fuente de la Mora', '10104">Galapagar-La Navata', '37011">Getafe -Sector Tres', '37002">Getafe Centro', '60102">Getafe Industrial', '70200">Guadalajara', '35012">Humanes', '70111">La Garena', '35010">La Serna', '35608">Laguna', '35602">Las Aguilas', '37010">Las Margaritas Universidad', '10101">Las Matas', '35610">Las Retamas', '10005">Las Rozas', '10202">Las Zorreras', '35001">Leganes', '12005">Los Molinos', '12001">Los Negrales', '10007">Majadahonda', '70104">Meco', '18003">Mendez Alvaro', '35606">Mostoles', '35607">Mostoles el Soto', '18002">Nuevos Ministerios', '35703">Orcasitas', '37012">Parla', '35011">Parque Polvoranca', '10100">Pinar de las Rozas', '60103">Pinto', '18005">Piramides', '97100">Pitis', '10002">Pozuelo', '10000">Principe Pio', '35704">Puente Alcocer', '12020">Puerto de Navacerrada', '97201">Ramon y Cajal', '18001">Recoletos', '10205">Robledo de Chavela', '60107">San Cristobal de los Angeles', '60101">San Cristobal Industrial', '70101">San Fernando', '35604">San Jose de Valderas', '10201">San Yago', '70109">Santa Eugenia', '10206">Santa Maria de la Alameda', '18101">Sol', '70112">Soto del Henares', '70102">Torrejon de Ardoz', '10103">Torrelodones', '17004">Tres Cantos', '19001">Universidad P.Comillas', '98304">Valdebebas', '19002">ValdelasFuentes', '60104">Valdemoro', '70001">Vallecas', '70100">Vicalvaro', '10200">Villalba', '37001">Villaverde Alto', '60100">Villaverde Bajo', '10204">Zarzalejo', '35009">Zarzaquemada', '98305">Aeropuerto-T4', '70103">Alcala de Henares', '70107">Alcala de Henares-Universidad', '19003">Alcobendas-S.Sebast. de los Reyes', '35605">Alcorcon', '12002">Alpedrete', '35600">Aluche', '60200">Aranjuez', '10001">Aravaca', '70002">Asamblea de Madrid-Entrevias', '18000">Atocha', '70105">Azuqueca', '17009">Cantoblanco Universidad', '12006">Cercedilla', '17000">Chamartin', '60105">Ciempozuelos', '12004">Collado Mediano', '17005">Colmenar Viejo', '70108">Coslada', '12023">Cotos', '35603">Cuatro Vientos', '18004">Delicias', '35702">Doce de Octubre', '10010">El Barrial-C.Com.Pozuelo', '60109">El Casar', '10203">El Escorial', '17003">El Goloso', '70003">El Pozo', '35609">Embajadores', '35601">Fanjul', '17001">Fuencarral', '35002">Fuenlabrada', '98003">Fuente de la Mora', '10104">Galapagar-La Navata', '37011">Getafe -Sector Tres', '37002">Getafe Centro', '60102">Getafe Industrial', '70200">Guadalajara', '35012">Humanes', '70111">La Garena', '35010">La Serna', '35608">Laguna', '35602">Las Aguilas', '37010">Las Margaritas Universidad', '10101">Las Matas', '35610">Las Retamas', '10005">Las Rozas', '10202">Las Zorreras', '35001">Leganes', '12005">Los Molinos', '12001">Los Negrales', '10007">Majadahonda', '70104">Meco', '18003">Mendez Alvaro', '35606">Mostoles', '35607">Mostoles el Soto', '18002">Nuevos Ministerios', '35703">Orcasitas', '37012">Parla', '35011">Parque Polvoranca', '10100">Pinar de las Rozas', '60103">Pinto', '18005">Piramides', '97100">Pitis', '10002">Pozuelo', '10000">Principe Pio', '35704">Puente Alcocer', '12020">Puerto de Navacerrada', '97201">Ramon y Cajal', '18001">Recoletos', '10205">Robledo de Chavela', '60107">San Cristobal de los Angeles', '60101">San Cristobal Industrial', '70101">San Fernando', '35604">San Jose de Valderas', '10201">San Yago', '70109">Santa Eugenia', '10206">Santa Maria de la Alameda', '18101">Sol', '70112">Soto del Henares', '70102">Torrejon de Ardoz', '10103">Torrelodones', '17004">Tres Cantos', '19001">Universidad P.Comillas', '98304">Valdebebas', '19002">ValdelasFuentes', '60104">Valdemoro', '70001">Vallecas', '70100">Vicalvaro', '10200">Villalba', '37001">Villaverde Alto', '60100">Villaverde Bajo', '10204">Zarzalejo', '35009">Zarzaquemada']

b = []
for x in a:
    x = x.replace("\"", "")
    x = x.replace(">"," ")
    b.append(x)

c = []
for  x in b:
    a = x.split()
    c.append(a)

res = {}
for x in c:
    res[x[1]]= x[0]

print(res)

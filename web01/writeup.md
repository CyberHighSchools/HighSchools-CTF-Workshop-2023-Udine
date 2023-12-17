# 5th HighSchools CTF Workshop - Udine 2023

## [web] spider

Riuscirai a trovare i miei segreti?

La flag è divisa in due parti, dovrai trovarle entrambe e concatenarle per ottenere la flag.

Site: [http://spider.challs.cyberhighschools.it](http://spider.challs.cyberhighschools.it)

### Soluzione

Il sito è composto da una pagina statica che non presenta vulnerabilità, ma contiene il seguente indizio:

> Pensa come uno [spider](https://it.wikipedia.org/wiki/Crawler)

Questo ci fa intuire che le due parti della flag si trovano in due percorsi che uno spider riuscirebbe a trovare.

In particolare:

- il file [robots.txt](https://it.wikipedia.org/wiki/Protocollo_di_esclusione_robot) ci informa dell'esistenza del file `supe3s3cretf0lder/flag1.txt`, contenente la prima parte;
- il file [sitemap.xml](https://it.wikipedia.org/wiki/Sitemap) ci indica il percorso del file contenente la seconda parte, `standardNonSecretFolder/flag2.txt`.

Concatenando le due parti della flag otteniamo la flag `flag{s3mbr1_un0_sp1d3R}`.

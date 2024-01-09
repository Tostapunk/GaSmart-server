# GaSmart-server
Tramite il server vengono fornite le API per la richiesta dei distributori.
## Come avviarlo
Per avviare il server utilizzare:
- `make start`, per avviare in modalità normale
- `make debug`, per avviare in modalità debug

## Richiesta
`base_url/get/coord/raggio/carburante/numero_risultati/kml/sort`

### Sorting keys
- `spesa_consumi`: minimizza il rapporto spesa/consumi
- `distanza`: minimizza la distanza
- `sostenibile`: minimizza i consumi
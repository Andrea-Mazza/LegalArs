IMPORTANTISSIMO:
- Quando crei un'app per un nuovo servizio, è di fondamentale importanza che l'app e app_name abbiamo la stessa stringa.
- Inoltre, la vista per la singola pratica deve essere chiamata 'pratica_details' e l'url deve essere: path('pratica/<int:pratica_id>', views.pratica_details, name='pratica_details')
- Quando crei un nuovo modello per una pratica di un servizio, aggiungilo in dashboard/signals

# Esempio di Invocazione: Content Performance Analyzer

## Prompt da copiare e incollare:

> Usa la skill "content-performance-analyzer" per analizzare le performance dei contenuti.
>
> Analizza il file CSV `test_data/sample_metrics.csv` e fornisci:
>
> 1. **Top 5 contenuti** per engagement rate
> 2. **Performance per categoria** con metriche medie
> 3. **Trend identificati** nel periodo analizzato
> 4. **3 raccomandazioni** actionable per il prossimo mese
>
> Presenta i risultati in formato report markdown con tabelle dove appropriato.

## Output atteso:

Un report completo con:
- Executive summary con KPI principali
- Classifica top performer
- Breakdown per categoria
- Trend analysis
- Raccomandazioni prioritizzate (Quick Win, Strategic, Experiment)

## Analisi avanzate da richiedere:

```
Oltre all'analisi base, rispondi a queste domande:
- Quale categoria ha il miglior ROI in termini di engagement/views?
- C'è correlazione tra giorno di pubblicazione e performance?
- Quali titoli hanno pattern comuni nei top performer?
```

## Note:

- La skill viene invocata menzionando il nome tra virgolette
- Il CSV deve avere almeno: content_id, title, publish_date, views, engagement, clicks
- Servono minimo 5-10 contenuti per analisi significative
- I benchmark sono medie di settore, calibra sul tuo storico

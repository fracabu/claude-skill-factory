# Esempio di Invocazione: Presentation Generator

## Prompt da copiare e incollare:

> Usa la skill "presentation-generator" per creare una presentazione completa.
>
> **Topic**: Digital Marketing Trends 2025
> **Audience**: Marketing managers di aziende medio-grandi
> **Goal**: Educare sulle tendenze e fornire azioni concrete
> **Duration**: 15 minuti (circa 12 slide)
> **Style**: Corporate, professionale ma accessibile
>
> **Punti chiave da includere**:
> - AI e personalizzazione
> - Dominanza dei contenuti video
> - Marketing privacy-first
> - Ottimizzazione voice search
> - Messaggi di sostenibilità
>
> Per ogni slide genera:
> 1. Headline accattivante (max 8 parole)
> 2. 3-5 bullet point o contenuto principale
> 3. Speaker notes dettagliate (cosa dire)
> 4. Prompt per generare immagine con DALL-E/Midjourney
> 5. Alternative: keywords per stock photo
>
> Colori brand: Blu #2563EB, Verde accent #10B981

---

## Output atteso:

Una presentazione strutturata in markdown con 12 slide complete:

```markdown
# Digital Marketing Trends 2025

## Slide 1: Title
### Content
# Il Marketing del Futuro è Già Qui
## Trend e Strategie per il 2025
[Nome] | [Data]

### Visual Direction
🎨 **AI Prompt**: "Futuristic digital marketing concept, abstract data flows
and social media icons, corporate blue color scheme, clean professional style,
16:9 presentation background"

### Speaker Notes
Benvenuti. Oggi esploreremo i 5 trend che stanno ridefinendo il marketing...

---

## Slide 2: Agenda
...
```

---

## Varianti di richiesta:

### Per un Pitch Deck:
```
Crea un pitch deck di 10 slide per presentare la mia startup [nome]
agli investitori. Il prodotto è [descrizione]. Includi: problema,
soluzione, mercato, traction, team, ask.
```

### Per una Presentazione Educativa:
```
Genera una presentazione didattica di 15 slide su [argomento] per
studenti universitari. Stile: engaging, usa analogie e esempi pratici.
```

### Per un Report Trimestrale:
```
Crea una presentazione di business review Q4 2024 con: risultati vs
obiettivi, highlight, sfide, piano Q1 2025. Include placeholder per grafici.
```

---

## Per generare il PowerPoint:

Dopo aver ottenuto l'output markdown, usa lo script Python:

```bash
# Installa dipendenze
pip install python-pptx Pillow

# Salva l'output in un file .md
# Poi esegui:
python presentation_builder.py
```

---

## Tips per risultati migliori:

1. **Sii specifico sull'audience**: "CEO non tecnici" è meglio di "manager"
2. **Indica il tempo**: Aiuta a calibrare la densità dei contenuti
3. **Fornisci dati**: Se hai statistiche specifiche, includile
4. **Specifica il tono**: Formale, casual, ispiratore, urgente
5. **Esempi di riferimento**: "Stile simile alle presentazioni Apple"

---

## Note:

- La skill genera **struttura e contenuti**, non il file .pptx direttamente
- I **prompt immagine** sono pronti per DALL-E, Midjourney o Leonardo AI
- Le **stock keywords** funzionano su Unsplash, Pexels, Shutterstock
- Lo **script Python** trasforma l'output in PowerPoint reale
- Per grafici complessi, usa Excel/Google Sheets e inserisci come immagine

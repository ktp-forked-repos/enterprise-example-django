# Example Python Django web app

This example web app demonstrates how developers can integrate with the Genomelink Enterprise API from a Django application.


## Live demo

You can try a [live demo here](https://token-example-django.genomelink.io/) using the example genome files below.

- [Example valid genome file](https://github.com/genomelink/enterprise-example-django/files/2541378/example.valid.min.txt)
  - When uploading this valid genome file via the "Connect my DNA" button in the live demo, the data will be successfully validated and the report data will be displayed.
- [Example "invalid" genome file](https://github.com/genomelink/enterprise-example-django/files/2541379/example.invalid.min.txt)
  - When uploading this "invalid" genome file via the "Connect my DNA" button in the live demo, the validation process will return an error and the user will be prompted to re-try the upload process with a different file.


## Requirements

- Python >= 3.6
- Django >= 1.11


## How to run

Install required packages.

```bash
$ pip install -r requirements.txt
```

Export `GENOMELINK_CLIENT_ID` and `GENOMELINK_CLIENT_SECRET` as environment variables.

```bash
$ export GENOMELINK_CLIENT_ID=<your_client_id>
$ export GENOMELINK_CLIENT_SECRET=<your_client_secret>
```

Run the app on your localhost.

```bash
$ python manage.py runserver
```

Then, open `http://localhost:8000` in your web browser.


## How it works

By inserting the following HTML snippet in your template, you can embed the "Connect my DNA" button on your website.

```html
<form action="/" method="POST">
  <script src="https://sdk.genomelink.io/genomelink.js"
          class="genomelink-button"
          data-key="{{ GENOMELINK_CLIENT_ID }}">
  </script>
</form>
```

![screen-shot-embed-button](https://user-images.githubusercontent.com/1478450/47902468-77861680-dec5-11e8-99dd-7535b9e17153.png)

When a user clicks the "Connect my DNA" button, a window for uploading their DNA data as a genome file will pop up.

![screen-shot-file-input](https://user-images.githubusercontent.com/1478450/47902473-79e87080-dec5-11e8-8e1d-3d3e406ba2b2.png)

The genome file is validated and analysed by Genomelink. If the user uploads invalid data, they are prompted to retry the upload process.

![screen-shot-failed](https://user-images.githubusercontent.com/1478450/47902497-866cc900-dec5-11e8-9d77-74e32465f708.png)

After they successfully upload their data via this window, a POST request is sent to the URL specified in the `action` form attribute containing an access token as POST parameter.

```python
token = request.POST.get('genomelinkToken')
```

This token is issued once per user. With this token you can acquire the DNA report for the user using the Genomelink SDK.

```python
reports = genomelink.Report.fetch(token=token, client_secret=settings.GENOMELINK_CLIENT_SECRET)
```

![screen-shot-completed](https://user-images.githubusercontent.com/1478450/47902485-81a81500-dec5-11e8-84da-6485b6d528d0.png)

After fetching the report data you can continue to use it inside your application and/or store it in your database. 

![screen-shot-render-reports](https://user-images.githubusercontent.com/1478450/47902487-840a6f00-dec5-11e8-9d6e-ba555249a62b.png)

## SDK reference

`genomelink.Report` object

| attributes        | description                                            | example              |
|-------------------|--------------------------------------------------------|----------------------|
| report.name       | displayable `name` of the genetic tendency report      | Diet recommendation  |
| report.score.code | `code` of the interpreted genetic tendency of the user | `high-protein`       |
| report.score.text | displayable `text` of corresponding `code`             | High protein diet    |

E.g.,

```
>>> reports = genomelink.Report.fetch(...)
>>> reports['diet-recommendation'].name
Diet recommendation
>>> reports['diet-recommendation'].score.code
`high-protein`
>>> reports['diet-recommendation'].score.text
High protein diet
```

### List of reports

| key                                     | `report.name` | `report.score.code`                                                                      |
|-----------------------------------------|---------------|--------------------------------------------------------------------------------------|
| `diet-recommendation`                   | Diet recommendation                   | `high-protein`, `low-fat`,  `low-carb`, `inconclusive` |
| `vitamin-a`                             | Vitamin A   | `higher`, `slightly-higher`, `intermediate`, `slightly-lower`, `lower`, `inconclusive` |
| `vitamin-b12`                           | Vitamin B12 | same as above |
| `vitamin-d`                             | Vitamin D   | same as above |
| `vitamin-e`                             | Vitamin E   | same as above |
| `response-to-vitamin-e-supplementation` | Response to Vitamin E Supplementation | same as above |
| `folate`                                | Folate	                              | same as above |
| `calcium`                               | Calcium                               | same as above |
| `magnesium`                             | Magnesium                             | same as above |
| `phosphorus`                            | Phosphorus                            | same as above |
| `iron`                                  | Iron                                  | same as above |
| `alpha-linolenic-acid`                  | Alpha-Linolenic Acid               	  | same as above |
| `beta-carotene`                         | Beta-Carotene                         | same as above |
| `blood-glucose`                         | Blood Glucose                         | same as above |
| `sleep-duration`                        | Sleep Duration                        | same as above |
| `egg-allergy`                           | Egg Allergy                           | same as above |
| `milk-allergy`                          | Milk Allergy                          | same as above |
| `endurance-performance`                 | Endurance Performance                 | same as above |
| `caffeine-metabolite-ratio`             | Caffeine Metabolite Ratio             | same as above |
| `caffeine-consumption`                  | Caffeine Consumption                  | same as above |



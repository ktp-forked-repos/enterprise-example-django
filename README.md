# Example Python Django web app

This example web app demonstrates how developers can integrate Genomelink Enterprise API with Django.


## Live demo

You can try [live demo here](https://token-example-django.genomelink.io/) with example DNA data below.

- [Example valid DNA data](https://github.com/genomelink/enterprise-example-django/files/2541378/example.valid.min.txt)
  - By uploading this valid DNA data via "Connect my DNA" button in the live demo, the data will be successfully interpreted and its reports data will be displayed.
- [Example "invalid" DNA data](https://github.com/genomelink/enterprise-example-django/files/2541379/example.invalid.min.txt)
  - By uploading this "invalid" DNA data via "Connect my DNA" button in the live demo, the validation process will abort interpreting it and the user will be prompted to re-try uploading with another file.


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


## List of reports

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


## How it works

By embedding a HTML tag as below, you can put "Connect my DNA" button in your website.

```html
<form action="/" method="POST">
  <script src="https://sdk.genomelink.io/genomelink.js"
          class="genomelink-button"
          data-key="{{ GENOMELINK_CLIENT_ID }}">
  </script>
</form>
```

![screen-shot-01](https://user-images.githubusercontent.com/1478450/38173924-656da8e6-3600-11e8-844f-3a4f5bf51743.png)

When users click the "Connect my DNA" button, a window for registering their DNA will pop up.

![screen-shot-02](https://user-images.githubusercontent.com/1478450/39857476-8358a586-546e-11e8-835f-7ecadd198208.png)

After they successfully upload their data via this window, you will acquire an access token in server-side as POST parameter.

```python
token = request.POST.get('genomelinkToken')
```

This token is issued per user, thus by using this token, you can call the API endpoint for acquiring DNA report of each user from Genomelink API server.

![screen-shot-completed](https://user-images.githubusercontent.com/1478450/43304742-3577ff40-91b0-11e8-8fc3-dbadff61ae12.png)

Now you can render users DNA reports within a view `/` where we set as a `action` attribute of the form.

```html
<form action='/' method='POST'>
```

![screen-shot-render-reports](https://user-images.githubusercontent.com/1478450/43304748-39f822a2-91b0-11e8-8b51-3b48f69e2976.png)

Even if users upload invalid data, they can retry uploading.

![screen-shot-failed](https://user-images.githubusercontent.com/1478450/43304745-37ac5b44-91b0-11e8-8ee6-008861764c69.png)

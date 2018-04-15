# CEPRange

Show the data from a given CEP range (Brazilian postal code)

## Configuration

* Install python version 3
* Install dependencies running `pip3 install -r requirements.txt`
* Choose de cep range:

  * Open the file ceprange.py, change de variable `initial_cep` for the start, and `final_cep` for the end, both use only number. eg.:

  ```python
  initial_cep = 69049090
  final_cep = 69055660
  ```

## Usage

```bash
python3 ceprange.py
```

You will going to see the CEP in this format:

```csv
cep;estado;cidade;logradouro
```

eg.:

```csv
69020700;AM;Manaus;Centro;Vila Soares
69020720;AM;Manaus;AM;Centro;Vila Portela
```

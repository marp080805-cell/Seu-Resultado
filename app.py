import argparse
import csv
import io
import urllib.request

DEFAULT_SHEET_ID = "1aZeWcd1p9decL2-CpZRigQ0CRZrRADEtLOqFKm4PHnU"
CSV_EXPORT = "https://docs.google.com/spreadsheets/d/{}/export?format=csv"

def load_leads_from_sheet(sheet_id: str):
    """Download leads from a public Google Sheet and return as list of dicts."""
    url = CSV_EXPORT.format(sheet_id)
    with urllib.request.urlopen(url) as response:
        data = response.read().decode("utf-8")
    return list(csv.DictReader(io.StringIO(data)))


def load_leads_from_file(path: str):
    """Load leads from a local CSV file."""
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main():
    parser = argparse.ArgumentParser(
        description="Ferramenta simples para cold calls baseada em uma planilha Google"
    )
    parser.add_argument(
        "--sheet-id", default=DEFAULT_SHEET_ID, help="ID da planilha do Google Sheets"
    )
    parser.add_argument(
        "--csv", help="Caminho para um arquivo CSV local (ignora --sheet-id se informado)"
    )
    args = parser.parse_args()

    try:
        if args.csv:
            leads = load_leads_from_file(args.csv)
        else:
            leads = load_leads_from_sheet(args.sheet_id)
    except Exception as exc:
        print(f"Falha ao carregar leads: {exc}")
        return

    if not leads:
        print("Nenhum lead encontrado.")
        return

    outcomes = {"s": "sucesso", "n": "nao atendeu", "p": "passar"}
    results = []

    for lead in leads:
        print("\n--- Próximo contato ---")
        for key, value in lead.items():
            print(f"{key}: {value}")
        action = input("Resultado (s=sucesso, n=nao atendeu, p=passar, q=sair): ").strip().lower()
        if action == "q":
            break
        resultado = outcomes.get(action, "indefinido")
        results.append({**lead, "resultado": resultado})

    if results:
        fieldnames = list(results[0].keys())
        with open("results.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(results)
        print(f"Resultados salvos em results.csv ({len(results)} registros).")


if __name__ == "__main__":
    main()

 [ "entry_id", "date_collected", "location", "language_dialect", "context_tag", "manipulation_trigger", "raw_data_text", "key_slang_words_used", "integrity_verification" ]
def validate_dataset(file_path): print("--- Running Schema Validation ---") try: with open(file_path, 'r', encoding='utf-8') as f: data = json.load(f) except Exception as e: print(f"JSON Syntax Error: Could not parse file. Details: {e}") return False
if not isinstance(data, list): print("Structure Error: Root element must be a JSON array.") return False
seen_ids = set() errors = 0
for idx, entry in enumerate(data, start=1): entry_id = entry.get("entry_id", f"Entry #{idx}")
  if entry.get("entry_id") in seen_ids: print(f"Duplicate entry_id found: {entry.get('entry_id')}") errors += 1 else: if entry.get("entry_id"): seen_ids.add(entry.get("entry_id"))
for field in REQUIRED_FIELDS: if field not in entry: print(f"Missing required field: {field} in {entry_id}") errors += 1 elif entry[field] is None or entry[field] == "": print(f"Field {field} is empty in {entry_id}") errors += 1 elif field == "key_slang_words_used" and not isinstance(entry[field], list): print(f"Field key_slang_words_used must be a list in {entry_id}") errors += 1
if errors == 0: print(f"SUCCESS: All {len(data)} entries passed schema validation!") return True else: print(f"FAILURE: Validation failed with {errors} error(s).") return False
if name == "main": target_file = sys.argv[1] if len(sys.argv) > 1 else "data/sample_entries.json" success = validate_dataset(target_file) sys.exit(0 if success else 1)

import os

def debug_load():
    statement = ""
    count_insert = 0
    count_total = 0
    
    with open('data.sql', 'r', encoding='utf-8') as f:
        for line in f:
            stripped = line.strip()
            if not stripped or stripped.startswith('--') or stripped.startswith('/*'):
                continue
            
            statement += line
            
            if stripped.endswith(';'):
                count_total += 1
                clean_stmt = statement.strip()
                if clean_stmt.upper().startswith('INSERT INTO'):
                    count_insert += 1
                    print(f"Found INSERT: {clean_stmt[:50]}...")
                else:
                     # Print what else we found to see if we missed valid inserts due to parsing
                     if len(clean_stmt) > 50:
                        print(f"Found OTHER: {clean_stmt[:50]}...")
                     else:
                        print(f"Found OTHER: {clean_stmt}")

                statement = ""

    print(f"Total statements ending in ; found: {count_total}")
    print(f"Total INSERT statements found: {count_insert}")

if __name__ == "__main__":
    debug_load()

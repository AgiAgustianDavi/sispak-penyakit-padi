def min_cf(*args):
    return min(args)

def max_cf(*args):
    return max(args)

def forward_chaining(input_data):
    # Daftar rule yang menghasilkan "Terserang penyakit" dan nilai CF-nya
    cf_list = []

    # RULE 5: IF ada bercak = ya THEN kondisi_daun = Not ok (CF = 0.85)
    if input_data["ada_bercak"] == "ya":
        cf_evidence = float(input_data["cf_ada_bercak"])
        cf_list.append(0.85 * cf_evidence)

    # RULE 6: IF kuning_kering = ya AND ada bercak = tidak THEN kondisi_daun = Not ok (CF = 0.8)
    if input_data["kuning_kering"] == "ya" and input_data["ada_bercak"] == "tidak":
        cf_evidence = float(input_data["cf_kuning_kering"])
        cf_list.append(0.8 * cf_evidence)

    # RULE 8: IF kerdil = ya THEN kondisi_batang = Not ok (CF = 0.8)
    if input_data["kerdil"] == "ya":
        cf_evidence = float(input_data["cf_kerdil"])
        cf_list.append(0.8 * cf_evidence)

    # RULE 9: IF busuk = ya THEN kondisi_batang = Not ok (CF = 0.85)
    if input_data["busuk"] == "ya":
        cf_evidence = float(input_data["cf_busuk"])
        cf_list.append(0.85 * cf_evidence)

    # RULE 1: IF kondisi_daun = Ok AND terserang hama = ya THEN terserang penyakit (CF = 0.85)
    if input_data["ada_bercak"] == "tidak" and input_data["kuning_kering"] == "tidak" and input_data["ters_hama"] == "ya":
        cf_evidence = float(input_data["cf_ters_hama"])
        cf_list.append(0.85 * cf_evidence)

    # RULE 3: IF kondisi_daun = Ok AND terserang hama = tidak AND kondisi_batang = Not ok THEN terserang penyakit (CF = 0.8)
    if (input_data["ada_bercak"] == "tidak" and input_data["kuning_kering"] == "tidak" and
        input_data["ters_hama"] == "tidak" and (input_data["kerdil"] == "ya" or input_data["busuk"] == "ya")):
        cf_list.append(0.8)

    # RULE 4: IF kondisi_daun = Not ok THEN terserang penyakit (CF = 0.95)
    if input_data["ada_bercak"] == "ya" or input_data["kuning_kering"] == "ya":
        cf_list.append(0.95)

    # === GABUNGKAN CF ===
    def combine_cf(cf_values):
        if not cf_values:
            return 0
        result = cf_values[0]
        for cf in cf_values[1:]:
            result = result + cf * (1 - result)
        return round(result, 3)

    final_cf = combine_cf(cf_list)

    if final_cf >= 0.5:
        return f"Terserang penyakit (CF: {final_cf})"
    elif final_cf > 0:
        return f"Kemungkinan kecil terserang (CF: {final_cf})"
    else:
        return "Tidak terserang penyakit (CF: 0.0)"
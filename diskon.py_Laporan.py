// ================================
// KALKULATOR DISKON - CLEAN CODE
// ================================

const BATAS_HARGA_MURAH = 50000;

function hitungHargaSetelahDiskon(hargaAwal, persenDiskon) {
    const potongan = hargaAwal * (persenDiskon / 100);
    return hargaAwal - potongan;
}

function tentukanStatusHarga(hargaAkhir) {
    return hargaAkhir < BATAS_HARGA_MURAH ? "Murah" : "Mahal";
}

function tampilkanHasil(hargaAwal, persenDiskon) {
    const hargaAkhir = hitungHargaSetelahDiskon(hargaAwal, persenDiskon);
    const status = tentukanStatusHarga(hargaAkhir);

    console.log(`Harga awal: Rp${hargaAwal}`);
    console.log(`Diskon: ${persenDiskon}%`);
    console.log(`Harga akhir: Rp${hargaAkhir}`);
    console.log(`Status: ${status}`);
    console.log("------------------------");
}

// Data transaksi (bisa dikembangkan dari array/API)
const transaksiList = [
    { hargaAwal: 100000, diskon: 20 },
    { hargaAwal: 200000, diskon: 30 }
];

transaksiList.forEach(transaksi => {
    tampilkanHasil(transaksi.hargaAwal, transaksi.diskon);
});

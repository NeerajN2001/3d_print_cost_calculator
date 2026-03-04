const data = JSON.parse(localStorage.getItem("invoiceData"));

company.textContent = data.company;
address.textContent = data.address;
contact.textContent = data.contact;
invoiceNumber.textContent = data.invoiceNumber;
date.textContent = data.date;

const tbody = document.getElementById("rows");
tbody.innerHTML = "";

data.items.forEach(item => {
  tbody.innerHTML += `
  <tr>
    <td>${item.file}</td>
    <td>${item.printer}</td>
    <td>${item.nozzle} mm</td>
    <td>${item.material}</td>
    <td>${item.weight} g</td>
    <td>${item.hours.toFixed(2)}</td>
    <td>₹ ${item.total.toFixed(2)}</td>
  </tr>
  `;
});

grandTotal.textContent = data.grandTotal.toFixed(2);

if (data.signature) {
  document.getElementById("signatureImg").src = data.signature;
}
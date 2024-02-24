const yesBtn = document.getElementById('yes');

// ✅ Set the radio button to checked
yesBtn.checked = true;

// ✅ Set the radio button to unchecked
yesBtn.checked = false;
    

document.addEventListener("DOMContentLoaded", function () {
    const itemDetailsRadio = document.getElementById("yes");
    const inventoryRadio = document.getElementById("no");
    const purchaseOrdersRadio = document.getElementById("maybe");
    const lookupDetailsRadio = document.getElementById("mayb");

    const filtersItemDetails = document.querySelector(".filters-item_details");
    const filtersInventory = document.querySelector(".filters-inventory");
    const filtersPurchaseOrders = document.querySelector(".filters-Purchase_orders");
    const filtersLookupDetails = document.querySelector(".filters-lookup_details");

    itemDetailsRadio.addEventListener("change", function () {
        if (itemDetailsRadio.checked) {
            filtersItemDetails.classList.remove("hidden");
            filtersInventory.classList.add("hidden");
            filtersPurchaseOrders.classList.add("hidden");
            filtersLookupDetails.classList.add("hidden");
        }
    });

    inventoryRadio.addEventListener("change", function () {
        if (inventoryRadio.checked) {
            filtersItemDetails.classList.add("hidden");
            filtersInventory.classList.remove("hidden");
            filtersPurchaseOrders.classList.add("hidden");
            filtersLookupDetails.classList.add("hidden");
        }
    });

    purchaseOrdersRadio.addEventListener("change", function () {
        if (purchaseOrdersRadio.checked) {
            filtersItemDetails.classList.add("hidden");
            filtersInventory.classList.add("hidden");
            filtersPurchaseOrders.classList.remove("hidden");
            filtersLookupDetails.classList.add("hidden");
        }
    });

    lookupDetailsRadio.addEventListener("change", function () {
        if (lookupDetailsRadio.checked) {
            filtersItemDetails.classList.add("hidden");
            filtersInventory.classList.add("hidden");
            filtersPurchaseOrders.classList.add("hidden");
            filtersLookupDetails.classList.remove("hidden");
        }
    });
});



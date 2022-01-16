//using selectors inside the element
const mockTestViewRslts = document.querySelectorAll(".mockTestViewRslt");

mockTestViewRslts.forEach(function (mockTestViewRslt) {
    const btn = mockTestViewRslt.querySelector(".mockTestViewRslt-btn");
    // console.log(btn);

    btn.addEventListener("click", function () {
        // console.log(mockTestViewRslt);

        mockTestViewRslts.forEach(function (item) {
            if (item !== mockTestViewRslt) {
                item.classList.remove("mocktestShow-text");
            }
        });

        mockTestViewRslt.classList.toggle("mocktestShow-text");
    });
});
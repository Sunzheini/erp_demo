        function fShowHideProcessForm() {
            let x = document.getElementById("process_form");
            if (x.style.display === "none") {
                x.style.display = "block";
            } else {
                x.style.display = "none";
            }
        }

        function fShowHideProcessStepForm() {
            let x = document.getElementById("process_step_form");
            if (x.style.display === "none") {
                x.style.display = "block";
            } else {
                x.style.display = "none";
            }
        }

        function fShowHideRequirementForm() {
            let x = document.getElementById("requirement_form");
            if (x.style.display === "none") {
                x.style.display = "block";
            } else {
                x.style.display = "none";
            }
        }

        function fShowHideSearchForm() {
            let x = document.getElementById("search_form");
            let y = document.getElementById("search_form_container")
            if (x.style.display === "block") {
                x.style.display = "none";
                y.style.display = "none";
            } else {
                x.style.display = "block";
                y.style.display = "block";
            }
        }

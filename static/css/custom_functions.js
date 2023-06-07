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

        function fShowHideOrgForm() {
            let x = document.getElementById("main-container");
            if (x.style.display === "none") {
                x.style.display = "block";
            } else {
                x.style.display = "none";
            }
        }

        function fShowHideProcessMenu() {
            let x = document.getElementById('dynamic-buttons')
            let y = document.getElementById('second-hr')
            if (x.style.display === 'none') {
                x.style.display = 'block';
                y.style.marginTop = '15px';
            } else {
                x.style.display = 'none';
                y.style.marginTop = '4px';
            }
        }

        function fShowHideAssignmentForm() {
            let x = document.getElementById("assignment-form");
            if (x.style.display === "none") {
                x.style.display = "block";
            } else {
                x.style.display = "none";
            }
        }

        function fShowHideAssignmentForm2() {
            let x = document.getElementById("assignment-form2");
            if (x.style.display === "none") {
                x.style.display = "block";
            } else {
                x.style.display = "none";
            }
        }

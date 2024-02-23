function calculations_on_loose_focus() {
    const myForm = document.getElementsByClassName('div-custom-form')[0]

    myForm.addEventListener('focusout', function(event) {
        if (event.target.tagName === 'INPUT') {
            recalculate();
        }
    });

    function recalculate() {
        const material1_cost_rate = document.getElementById('id_material1_cost_rate').value;
        const material1_price = document.getElementById('id_material1_price').value;
        let material1_total_cost = document.getElementById('material1_total');
        let result = material1_cost_rate * material1_price;

        if (material1_total_cost) {
            material1_total_cost.innerText = result;
        }

        // -----------------------------------------------------------------------------------------
        const material2_cost_rate = document.getElementById('id_material2_cost_rate').value;
        const material2_price = document.getElementById('id_material2_price').value;
        let material2_total_cost = document.getElementById('material2_total');
        let result2 = material2_cost_rate * material2_price;

        if (material2_total_cost) {
            material2_total_cost.innerText = result2;
        }

        // -----------------------------------------------------------------------------------------
        const material3_cost_rate = document.getElementById('id_material3_cost_rate').value;
        const material3_price = document.getElementById('id_material3_price').value;
        let material3_total_cost = document.getElementById('material3_total');
        let result3 = material3_cost_rate * material3_price;

        if (material3_total_cost) {
            material3_total_cost.innerText = result3;
        }

        // -----------------------------------------------------------------------------------------
        const material4_cost_rate = document.getElementById('id_material4_cost_rate').value;
        const material4_price = document.getElementById('id_material4_price').value;
        let material4_total_cost = document.getElementById('material4_total');
        let result4 = material4_cost_rate * material4_price;

        if (material4_total_cost) {
            material4_total_cost.innerText = result4;
        }

        // -----------------------------------------------------------------------------------------
        const material5_cost_rate = document.getElementById('id_material5_cost_rate').value;
        const material5_price = document.getElementById('id_material5_price').value;
        let material5_total_cost = document.getElementById('material5_total');
        let result5 = material5_cost_rate * material5_price;

        if (material5_total_cost) {
            material5_total_cost.innerText = result5;
        }

        // -----------------------------------------------------------------------------------------
        let materials = result + result2 + result3 + result4 + result5;
        let total_materials_cost = document.getElementById('total_materials_cost');
        if (total_materials_cost) {
            total_materials_cost.innerText = materials;
        }

        // -----------------------------------------------------------------------------------------
        const machine1_cost_rate = document.getElementById('id_machine1_cost_rate').value;
        const machine1_price = document.getElementById('id_machine1_price').value;
        let machine1_total_cost = document.getElementById('machine1_total');
        let result6 = machine1_cost_rate * machine1_price;

        if (machine1_total_cost) {
            machine1_total_cost.innerText = result6;
        }

        // -----------------------------------------------------------------------------------------
        const machine2_cost_rate = document.getElementById('id_machine2_cost_rate').value;
        const machine2_price = document.getElementById('id_machine2_price').value;
        let machine2_total_cost = document.getElementById('machine2_total');
        let result7 = machine2_cost_rate * machine2_price;

        if (machine2_total_cost) {
            machine2_total_cost.innerText = result7;
        }

        // -----------------------------------------------------------------------------------------
        const machine3_cost_rate = document.getElementById('id_machine3_cost_rate').value;
        const machine3_price = document.getElementById('id_machine3_price').value;
        let machine3_total_cost = document.getElementById('machine3_total');
        let result8 = machine3_cost_rate * machine3_price;

        if (machine3_total_cost) {
            machine3_total_cost.innerText = result8;
        }

        // -----------------------------------------------------------------------------------------
        const machine4_cost_rate = document.getElementById('id_machine4_cost_rate').value;
        const machine4_price = document.getElementById('id_machine4_price').value;
        let machine4_total_cost = document.getElementById('machine4_total');
        let result9 = machine4_cost_rate * machine4_price;

        if (machine4_total_cost) {
            machine4_total_cost.innerText = result9;
        }

        // -----------------------------------------------------------------------------------------
        const machine5_cost_rate = document.getElementById('id_machine5_cost_rate').value;
        const machine5_price = document.getElementById('id_machine5_price').value;
        let machine5_total_cost = document.getElementById('machine5_total');
        let result10 = machine5_cost_rate * machine5_price;

        if (machine5_total_cost) {
            machine5_total_cost.innerText = result10;
        }

        // -----------------------------------------------------------------------------------------

        let machines = result6 + result7 + result8 + result9 + result10;
        let total_machines_cost = document.getElementById('total_machines_cost');
        if (total_machines_cost) {
            total_machines_cost.innerText = machines;
        }

        // -----------------------------------------------------------------------------------------
        const position1_cost_rate = document.getElementById('id_position1_cost_rate').value;
        const position1_price = document.getElementById('id_position1_price').value;
        let position1_total_cost = document.getElementById('position1_total');
        let result11 = position1_cost_rate * position1_price;

        if (position1_total_cost) {
            position1_total_cost.innerText = result11;
        }

        // -----------------------------------------------------------------------------------------
        const position2_cost_rate = document.getElementById('id_position2_cost_rate').value;
        const position2_price = document.getElementById('id_position2_price').value;
        let position2_total_cost = document.getElementById('position2_total');
        let result12 = position2_cost_rate * position2_price;

        if (position2_total_cost) {
            position2_total_cost.innerText = result12;
        }

        // -----------------------------------------------------------------------------------------
        const position3_cost_rate = document.getElementById('id_position3_cost_rate').value;
        const position3_price = document.getElementById('id_position3_price').value;
        let position3_total_cost = document.getElementById('position3_total');
        let result13 = position3_cost_rate * position3_price;

        if (position3_total_cost) {
            position3_total_cost.innerText = result13;
        }

        // -----------------------------------------------------------------------------------------
        const position4_cost_rate = document.getElementById('id_position4_cost_rate').value;
        const position4_price = document.getElementById('id_position4_price').value;
        let position4_total_cost = document.getElementById('position4_total');
        let result14 = position4_cost_rate * position4_price;

        if (position4_total_cost) {
            position4_total_cost.innerText = result14;
        }

        // -----------------------------------------------------------------------------------------
        const position5_cost_rate = document.getElementById('id_position5_cost_rate').value;
        const position5_price = document.getElementById('id_position5_price').value;
        let position5_total_cost = document.getElementById('position5_total');
        let result15 = position5_cost_rate * position5_price;

        if (position5_total_cost) {
            position5_total_cost.innerText = result15;
        }

        // -----------------------------------------------------------------------------------------
        let positions = result11 + result12 + result13 + result14 + result15;
        let total_positions_cost = document.getElementById('total_positions_cost');
        if (total_positions_cost) {
            total_positions_cost.innerText = positions;
        }

        // -----------------------------------------------------------------------------------------
        const additional_expense_materials_cost_rate = document.getElementById('id_additional_expense_materials_cost_rate').value;
        let additional_expense_materials_total = document.getElementById('additional_expense_materials_total');
        let additional_expense_materials_cost = materials * additional_expense_materials_cost_rate;
        additional_expense_materials_total.innerText = additional_expense_materials_cost;

        // -----------------------------------------------------------------------------------------
        const additional_expense_machines_cost_rate = document.getElementById('id_additional_expense_machines_cost_rate').value;
        let additional_expense_machines_total = document.getElementById('additional_expense_machines_total');
        let additional_expense_machines_cost = machines * additional_expense_machines_cost_rate;
        additional_expense_machines_total.innerText = additional_expense_machines_cost;

        // -----------------------------------------------------------------------------------------
        const additional_expense_positions_cost_rate = document.getElementById('id_additional_expense_positions_cost_rate').value;
        let additional_expense_positions_total = document.getElementById('additional_expense_positions_total');
        let additional_expense_positions_cost = positions * additional_expense_positions_cost_rate;
        additional_expense_positions_total.innerText = additional_expense_positions_cost;

        // -----------------------------------------------------------------------------------------
        let total_direct_costs = document.getElementById('total_direct_costs');
        let total_additional_costs = document.getElementById('total_additional_costs');
        let total_costs = document.getElementById('total_costs');

        let direct_costs = materials + machines + positions;
        total_direct_costs.innerText = direct_costs;

        let additional_costs = additional_expense_materials_cost + additional_expense_machines_cost + additional_expense_positions_cost;
        total_additional_costs.innerText = additional_costs;

        let costs = direct_costs + additional_costs;
        total_costs.innerText = costs;

        // -----------------------------------------------------------------------------------------
        const profit = document.getElementById('id_profit').value;
        let final_price = document.getElementById('final_price');
        let result16 = costs * profit;

        if (final_price) {
            final_price.innerText = result16;
        }
    }
}

calculations_on_loose_focus();

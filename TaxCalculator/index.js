let bracket1=24000;
let bracket2=32333;
let bracket3=500000;
let bracket4=800000;
const band1=bracket1*0.1;
const band2=(bracket2-bracket1)*0.25;
const band3=(bracket3-bracket2)*0.3;
const band4=(bracket4-bracket3)*0.325;
const personal_relief=2400;
while(true){
    let grossMonthlySalary=window.prompt("Enter Salary");
    let grossPAYE=null;
    let housing_levy=null;
    let NSSF=null;
    console.log(typeof grossMonthlySalary);
    if(!isNaN(grossMonthlySalary)){
        grossMonthlySalary=Number(grossMonthlySalary);
        if(grossMonthlySalary<=0){
            window.alert("Enter a valid salary.Must be greater than 0 and only contain 0..9");
            break;
        }
        //First check if gross salary is greater than 9000
        if(grossMonthlySalary>9000){
            //It means you pay the entire tier 1
            NSSF=9000*0.06;
            //check tier 3
            if(grossMonthlySalary>108000){
                //Cap NSSF at 6480
                NSSF=6480;
            }
            //If i don't qualtify for tier 3,I autommatically qualify for tier 2 
            //For tier 2 I need to add to the current NSSF tax
            else{
                NSSF+=(grossMonthlySalary-9000)*0.06;
            }
        }
        //If its less just perform the normal 6% check
        else{
            NSSF=grossMonthlySalary*0.06;
        }
        let taxableIncome=grossMonthlySalary-NSSF;

        //grossPAYE calculations
        //Check first if you are in the first income bracket
        if(taxableIncome<=bracket1){
            //If you are paye -> direct
            grossPAYE=taxableIncome*0.10;
        }
        else if(taxableIncome<=bracket2){
            //If in second get by how much.
            //Then add tax from the previous brackets
            grossPAYE=(taxableIncome-bracket1)*0.25+band1;
        }
        else if(taxableIncome<=bracket3){
            //Same for the rest
            grossPAYE=(taxableIncome-bracket2)*0.30+(band1+band2);
        }
        else if(taxableIncome<=bracket4){
            grossPAYE=(taxableIncome-bracket3)*0.325+(band1+band2+band3);
        }
        else{
            grossPAYE=(taxableIncome-bracket4)*0.35+(band1+band2+band3+band4);
        }
        let netPAYE=Math.max(0,grossPAYE-personal_relief);
        let housing_levy=grossMonthlySalary*0.015;
        let SHIF=grossMonthlySalary*0.0275;
        let netSalary=Math.round(grossMonthlySalary-netPAYE-housing_levy-SHIF);
        console.log(`Net Salary: ${netSalary}`);
    }
    else{
            window.alert("Enter a valid number");
    }
}
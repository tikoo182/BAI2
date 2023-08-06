import { Component, Input, OnInit } from '@angular/core';
import { SharedService } from 'src/app/shared.service';
import { Color } from '@swimlane/ngx-charts'

@Component({
  selector: 'app-bai2',
  templateUrl: './bai2.component.html',
  styleUrls: ['./bai2.component.css'],
})
export class Bai2Component {


  constructor(private service: SharedService) {}

  question: string = '';
  rows: any[] = [];

  // Holds the data for the bar chart
  chartData: any[] = []; 
  view: [number, number] = [700, 400];

  indexCardData: { name: string; value: number; } | any;


  // Chart options
  showXAxis = true;
  showYAxis = true;
  gradient = false;
  showLegend = true;
  showXAxisLabel = true;
  xAxisLabel = 'Category';
  showYAxisLabel = true;
  yAxisLabel = 'Value';
  showLabels: boolean = true;
  isDoughnut: boolean = false;
  legendPosition: string = 'below';

  colorScheme: Color = {
    domain: ['#5AA454', '#A10A28', '#C7B42C', '#AAAAAA'],
  } as Color;

  ngOnInit(): void {}

  getData() {
    var val = this.question;
    this.service.Query(val).subscribe((res) => {
      this.rows = res;
      this.processDataForChart();
    });
  }

  processDataForChart() {
    // Clear previous chart data
    this.chartData = [];
  
    for (const row of this.rows) {
      let name: string | null = null;
      let value: number | null = null;
      for (const key in row) {
        if (row.hasOwnProperty(key)) {
          const val = row[key];
          if (typeof val === 'string') {
            // If the value is a string, use it as the name
            name = val;
          } else if (typeof val === 'number') {
            // If the value is a number, use it as the value
            value = val;
            break;
          }
        }
      }

      this.chartData.push({ name: name, value: value });
    }

    this.indexCardData = this.chartData.length > 0 ? this.chartData[0] : undefined;

  }
  

  
}




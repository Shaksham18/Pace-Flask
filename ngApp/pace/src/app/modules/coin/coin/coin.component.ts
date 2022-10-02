import { Component, OnInit } from '@angular/core';
import { CoinService } from '../coin.service';

@Component({
  selector: 'app-coin',
  templateUrl: './coin.component.html',
  styleUrls: ['./coin.component.css']
})
export class CoinComponent implements OnInit {
  coins = [];
  
  constructor(
    private coinService: CoinService
  ) { }

  ngOnInit(): void {
    this.coinService.getAllCoin().subscribe(res => {
      this.coins = res.data
    })
  }
  
}


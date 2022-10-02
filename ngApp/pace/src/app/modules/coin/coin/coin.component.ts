import { Component, OnDestroy, OnInit } from '@angular/core';
import { CoinService } from '../coin.service';

@Component({
  selector: 'app-coin',
  templateUrl: './coin.component.html',
  styleUrls: ['./coin.component.css']
})
export class CoinComponent implements OnInit,OnDestroy {
  coins = [];
  interval:any;
  constructor(
    private coinService: CoinService
  ) { }

  ngOnInit(): void {
    this.get_coin_data()
    this.interval = setInterval(() => {
      this.get_coin_data()
    },10000)
  }

  ngOnDestroy(): void {
    clearInterval(this.interval)
  }

  get_coin_data(){
    this.coinService.getAllCoin().subscribe(res => {
      this.coins = res.data
    })
  }
  
}


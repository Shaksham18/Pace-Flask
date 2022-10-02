import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { CoinRoutingModule } from './coin-routing.module';
import { CoinComponent } from './coin/coin.component';


@NgModule({
  declarations: [
    CoinComponent
  ],
  imports: [
    CommonModule,
    CoinRoutingModule
  ]
})
export class CoinModule { }

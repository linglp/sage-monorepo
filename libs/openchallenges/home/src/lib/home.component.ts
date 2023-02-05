import { Component } from '@angular/core';
import { ConfigService } from '@sagebionetworks/openchallenges/config';

@Component({
  selector: 'openchallenges-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss'],
})
export class HomeComponent {
  public appVersion: string;

  constructor(private readonly configService: ConfigService) {
    this.appVersion = this.configService.config.appVersion;
  }
}
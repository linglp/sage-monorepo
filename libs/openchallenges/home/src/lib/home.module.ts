import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { SharedUtilModule } from '@sagebionetworks/shared/util';
import { FooterComponent, UiModule } from '@sagebionetworks/openchallenges/ui';
import { HomeComponent } from './home.component';
import { ChallengeSearchModule } from './challenge-search/challenge-search.module';
import { ChallengeHostListModule } from './challenge-host-list/challenge-host-list.module';
import { ChallengeRegistrationModule } from './challenge-registration/challenge-registration.module';
import { FeaturedChallengeListModule } from './featured-challenge-list/featured-challenge-list.module';
import { SponsorListModule } from './sponsor-list/sponsor-list.module';
import { StatisticsViewerModule } from './statistics-viewer/statistics-viewer.module';
import { TopicsViewerModule } from './topics-viewer/topics-viewer.module';
import { HomeRoutingModule } from './home-routing.module';

@NgModule({
  declarations: [HomeComponent],
  imports: [
    CommonModule,
    HomeRoutingModule,
    UiModule,
    ChallengeHostListModule,
    ChallengeRegistrationModule,
    ChallengeSearchModule,
    FeaturedChallengeListModule,
    SponsorListModule,
    StatisticsViewerModule,
    TopicsViewerModule,
    SharedUtilModule,
    FooterComponent,
  ],
})
export class HomeModule {}
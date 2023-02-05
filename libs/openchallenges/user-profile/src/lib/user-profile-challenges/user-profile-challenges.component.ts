import { Component, Input } from '@angular/core';
import {
  User,
  UserService,
} from '@sagebionetworks/openchallenges/api-client-angular-deprecated';
import {
  Challenge,
  ChallengeSearchQuery,
  ChallengeService,
} from '@sagebionetworks/openchallenges/api-client-angular';
import { BehaviorSubject, switchMap } from 'rxjs';
import { assign } from 'lodash';

@Component({
  selector: 'openchallenges-user-profile-challenges',
  templateUrl: './user-profile-challenges.component.html',
  styleUrls: ['./user-profile-challenges.component.scss'],
})
export class UserProfileChallengesComponent {
  @Input() user!: User;
  challenges: Challenge[] = [];
  pageNumber = 0;
  pageSize = 12;
  totalChallengesCount = 0;

  private query: BehaviorSubject<ChallengeSearchQuery> =
    new BehaviorSubject<ChallengeSearchQuery>({});

  constructor(
    private challengeService: ChallengeService,
    private userService: UserService
  ) {}

  ngOnInit(): void {
    this.query
      .pipe(switchMap((query) => this.challengeService.listChallenges(query)))
      .subscribe((page) => {
        this.totalChallengesCount = page.totalElements;
        this.challenges = page.challenges;
      });
  }

  onPageChange(event: any) {
    const newQuery = assign(this.query.getValue(), {
      pageNumber: event.page,
      pageSize: event.rows,
    });
    this.query.next(newQuery);
  }
}
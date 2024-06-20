import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { QuestionService } from '../question.service';

@Component({
  selector: 'app-question',
  templateUrl: './question.component.html',
  styleUrls: ['./question.component.css']
})
export class QuestionComponent implements OnInit {
  question: any;
  currentIndex: number=0;

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private questionService: QuestionService
  ) {}

  ngOnInit(): void {
    this.route.params.subscribe(params => {
      this.currentIndex = +params['id'];
      this.question = this.questionService.getQuestions()[this.currentIndex];
    });
  }

  nextQuestion(): void {
    if (this.currentIndex < this.questionService.getQuestions().length - 1) {
      this.router.navigate(['/question', this.currentIndex + 1]);
    } else {
      this.router.navigate(['/results']);
    }
  }
}
import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { AgendaListComponent } from './components/agenda-list/agenda-list.component';
import { TopicDetailComponent } from './components/topic-detail/topic-detail.component';
import { SpeakerListComponent } from './components/speaker-list/speaker-list.component';

const routes: Routes = [
    { path: '', component: AgendaListComponent },
    { path: 'topics/new', component: TopicDetailComponent },
    { path: 'topics/:id', component: TopicDetailComponent },
    { path: ':id/speakers', component: SpeakerListComponent }
];

@NgModule({
    imports: [RouterModule.forChild(routes)],
    exports: [RouterModule]
})
export class AgendaRoutingModule {}

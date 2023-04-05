import random
import time
import uuid


def generate_uuid():
    return uuid.uuid4()


def produce_paper_clips(components, workers):
    paper_clips_produced = 0
    while components > 0 and workers > 0:
        total_time = 0
        production_rate = random.randint(1, 10) * workers
        components -= production_rate
        if components < 0:
            production_rate += components
            components = 0
        paper_clips_produced += production_rate
        total_time += production_time

        print(f'Total paper clips produced: {paper_clips_produced}')

        time.sleep(production_time)

    return {'clips_produced': paper_clips_produced, 'time': total_time}


def produce_components(raw_materials, workers):
    components_produced = 0
    total_time = 0
    while raw_materials > 0 and workers > 0:
        production_rate = random.randint(1, 5) * workers
        raw_materials -= production_rate
        if raw_materials < 0:
            production_rate += raw_materials
            raw_materials = 0
        components_produced += production_rate
        total_time += component_production_time

        print(f'Component with ID {generate_id()} created')
        time.sleep(component_production_time)

    return {'time': total_time, 'comp_produced': components_produced}


def manage_production(paper_clip_time, component_time, raw_materials, workers):
    paper_clips_produced = 0
    components_produced = 0
    total_time = 0

    while raw_materials > 0 and workers > 0:
        component_workers = workers // 2
        paper_clip_workers = workers - component_workers

        new_components, component_time_spent = produce_components(
            component_time, raw_materials, component_workers)
        raw_materials -= new_components
        components_produced += new_components
        total_time += component_time_spent

        new_paper_clips, paper_clip_time_spent = produce_paper_clips(
            paper_clip_time, components_produced, paper_clip_workers)
        components_produced -= new_paper_clips
        paper_clips_produced += new_paper_clips
        total_time += paper_clip_time_spent

    return paper_clips_produced, total_time


if __name__ == "__main__":
    paper_clip_production_time = 0.05
    component_production_time = 0.1
    total_raw_materials = 5000
    factory_workers = random.randrange(40, 50)

    paper_clips, time_spent = manage_production(
        paper_clip_production_time, component_production_time, total_raw_materials, factory_workers)
    print(
        f"Paper clips produced: {paper_clips}, Time spent: {time_spent} seconds")

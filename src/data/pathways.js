export const pathways = [
  {
    id: "biomedical",
    title: "Pre-biomedical engineering",
    short: "BME core",
    icon: "◈",
    description: "A balanced sequence across biology, chemistry, calculus, physics, computation, and engineering analysis.",
    terms: [
      { label: "Year 1 · Fall", courses: ["cell-biology", "general-chemistry-1", "calculus-1", "physics-mechanics"] },
      { label: "Year 1 · Spring", courses: ["general-chemistry-2", "calculus-2", "physics-em", "programming"] },
      { label: "Year 2 · Fall", courses: ["genetics", "organic-chemistry", "linear-algebra", "calculus-3"] },
      { label: "Year 2 · Spring", courses: ["biochemistry", "physiology", "differential-equations", "statistics"] },
      { label: "Year 3 · Fall", courses: ["statics-materials", "circuits", "transport", "cellular-biomechanics"] },
      { label: "Year 3 · Spring", courses: ["signals-control", "robotics", "biomaterials", "bioreactors", "geroscience"] },
    ],
  },
  {
    id: "robotics",
    title: "Robotics & mechatronics",
    short: "Robotics",
    icon: "⌘",
    description: "Prioritize mechanics, linear systems, circuits, computation, sensing, actuation, and safe closed-loop design.",
    terms: [
      { label: "Foundation", courses: ["calculus-1", "calculus-2", "physics-mechanics", "programming"] },
      { label: "Mathematical tools", courses: ["linear-algebra", "calculus-3", "differential-equations", "physics-em"] },
      { label: "Engineering core", courses: ["statics-materials", "circuits", "signals-control", "statistics"] },
      { label: "Integration", courses: ["robotics", "cell-biology", "transport", "physiology"] },
    ],
  },
  {
    id: "tissue",
    title: "Tissue engineering & regenerative design",
    short: "Tissue engineering",
    icon: "⌬",
    description: "Connect cell and matrix biology with transport, mechanics, biomaterials, bioreactors, and functional validation.",
    terms: [
      { label: "Biological foundation", courses: ["cell-biology", "general-chemistry-1", "calculus-1", "physics-mechanics"] },
      { label: "Molecular tools", courses: ["general-chemistry-2", "organic-chemistry", "genetics", "calculus-2"] },
      { label: "Systems & measurement", courses: ["biochemistry", "physiology", "statistics", "linear-algebra"] },
      { label: "Engineering core", courses: ["calculus-3", "differential-equations", "statics-materials", "circuits", "transport"] },
      { label: "Specialization", courses: ["cellular-biomechanics", "biomaterials", "bioreactors", "geroscience"] },
    ],
  },
  {
    id: "geroscience",
    title: "Geroscience & regenerative biology",
    short: "Geroscience",
    icon: "✳",
    description: "Build a mechanistic foundation in cell biology, genetics, physiology, biochemistry, statistics, and tissue function.",
    terms: [
      { label: "Biological foundation", courses: ["cell-biology", "general-chemistry-1", "calculus-1", "physics-mechanics"] },
      { label: "Molecular foundation", courses: ["general-chemistry-2", "genetics", "organic-chemistry", "calculus-2"] },
      { label: "Mechanisms & evidence", courses: ["biochemistry", "physiology", "statistics", "linear-algebra"] },
      { label: "Tissue context", courses: ["calculus-3", "differential-equations", "transport", "cellular-biomechanics", "biomaterials"] },
      { label: "Translation", courses: ["geroscience", "bioreactors", "circuits", "programming"] },
    ],
  },
];

